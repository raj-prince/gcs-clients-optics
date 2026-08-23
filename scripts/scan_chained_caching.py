#!/usr/bin/env python3
"""
Scanner for fsspec chained filesystems (blockcache, filecache, simplecache, dirfs, zip, etc.)
and caching mechanisms across open-source target repositories.
"""

import argparse
import io
import json
import os
import re
import sys
import tarfile
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

CHAIN_PROTOCOLS = {
    "blockcache",
    "filecache",
    "simplecache",
    "cached",
    "dir",
    "zip",
    "tar",
    "gzip",
    "bz2",
    "xz",
    "lzma",
}

CACHE_CLASSES = {
    "BlockCacheFileSystem": "BlockCache (block memory/disk caching)",
    "WholeFileCacheFileSystem": "WholeFileCache (complete file disk caching)",
    "SimpleCacheFileSystem": "SimpleCache (temporary local file caching)",
    "CachingFileSystem": "CachingFileSystem base implementation",
    "DirFileSystem": "DirFileSystem (subtree directory prefix wrapper)",
    "ZipFileSystem": "ZipFileSystem (in-memory ZIP archive wrapper)",
    "TarFileSystem": "TarFileSystem (in-memory TAR archive wrapper)",
}

CACHE_KEYWORDS = {
    "blockcache",
    "filecache",
    "simplecache",
    "block",
    "file",
    "mmap",
    "readahead",
    "parts",
    "bytes",
    "background",
    "none",
}


def load_repos(
    repo_file: Optional[str] = None, explicit_repos: Optional[List[str]] = None
) -> List[str]:
    """Load target repositories from JSON or arguments."""
    if explicit_repos:
        return explicit_repos

    target_path = (
        Path(repo_file)
        if repo_file
        else Path(__file__).resolve().parent.parent / "data" / "default_dependents.json"
    )
    if not target_path.exists():
        # Fallback to local workspace data path
        target_path = Path("/usr/local/google/home/princer/code/gcs-clients-optics/data/default_dependents.json")

    if not target_path.exists():
        print(f"[-] Repository file not found at: {target_path}", file=sys.stderr)
        return []

    try:
        data = json.loads(target_path.read_text(encoding="utf-8"))
        repos = []
        for pkg in data.get("packages", []):
            for dep in pkg.get("public_dependents", []):
                name = dep.get("name")
                if name and name not in repos:
                    repos.append(name)
        return repos
    except Exception as e:
        print(f"[-] Error loading {target_path}: {e}", file=sys.stderr)
        return []


def inspect_repository(
    repo_name: str, branch: str = "main"
) -> Tuple[str, Dict[str, Any]]:
    """Download tarball from codeload.github.com and extract chained filesystem and cache patterns."""
    findings: Dict[str, Any] = {
        "repo_name": repo_name,
        "repo_url": f"https://github.com/{repo_name}",
        "total_files": 0,
        "chained_urls": [],
        "cache_type_kwargs": [],
        "caching_fs_calls": [],
        "cached_class_refs": [],
    }

    tar_bytes = None
    successful_branch = branch
    for b in [branch, "main", "master"]:
        url = f"https://codeload.github.com/{repo_name}/tar.gz/refs/heads/{b}"
        req = urllib.request.Request(url, headers={"User-Agent": "GCS-Clients-Optics-Scanner"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status == 200:
                    tar_bytes = resp.read()
                    successful_branch = b
                    break
        except Exception:
            continue

    if not tar_bytes:
        return repo_name, findings

    try:
        with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode="r:gz") as tar:
            for member in tar.getmembers():
                if not member.isfile() or not member.name.endswith(".py"):
                    continue
                parts = member.name.split("/")
                clean_path = "/".join(parts[1:]) if len(parts) > 1 else parts[0]

                # Exclude build / docs / vendor directories
                if any(
                    p in {"docs", "doc", "examples", "example", "benchmark", "benchmarks", "build", "dist", "site-packages", "vendor", "third_party"}
                    for p in parts
                ):
                    continue

                f = tar.extractfile(member)
                if not f:
                    continue
                code = f.read().decode("utf-8", errors="ignore")
                findings["total_files"] += 1
                lines = code.splitlines()

                # 1. Chained URL syntax (e.g. blockcache::, simplecache::, filecache::, f"simplecache::{url}")
                for m in re.finditer(r'(?:f?[\'"])?(blockcache|filecache|simplecache|cached|dir|zip|tar)::[^\'"]*[\'"]?', code, re.IGNORECASE):
                    proto = m.group(1).lower()
                    line_no = code[:m.start()].count("\n") + 1
                    snippet = lines[line_no - 1].strip() if line_no <= len(lines) else ""
                    file_url = f"https://github.com/{repo_name}/blob/{successful_branch}/{clean_path}#L{line_no}"
                    findings["chained_urls"].append({
                        "file": clean_path,
                        "line": line_no,
                        "protocol": proto,
                        "match": m.group(0),
                        "snippet": snippet,
                        "file_url": file_url,
                    })

                # 2. cache_type keyword in open / filesystem calls & dictionary assignments
                for m in re.finditer(r'cache_type[\'"]?\s*\]?\s*[:=]\s*[\'"]([a-zA-Z0-9_-]+)[\'"]', code, re.IGNORECASE):
                    ct = m.group(1).lower()
                    if ct in CACHE_KEYWORDS:
                        line_no = code[:m.start()].count("\n") + 1
                        snippet = lines[line_no - 1].strip() if line_no <= len(lines) else ""
                        file_url = f"https://github.com/{repo_name}/blob/{successful_branch}/{clean_path}#L{line_no}"
                        findings["cache_type_kwargs"].append({
                            "file": clean_path,
                            "line": line_no,
                            "cache_type": ct,
                            "snippet": snippet,
                            "file_url": file_url,
                        })

                # 3. fsspec.filesystem('blockcache' | 'filecache' | 'simplecache' | 'dir' | 'zip' | 'tar')
                for m in re.finditer(r'filesystem\s*\(\s*[\'"](blockcache|filecache|simplecache|cached|dir|zip|tar)[\'"]', code, re.IGNORECASE):
                    proto = m.group(1).lower()
                    line_no = code[:m.start()].count("\n") + 1
                    snippet = lines[line_no - 1].strip() if line_no <= len(lines) else ""
                    file_url = f"https://github.com/{repo_name}/blob/{successful_branch}/{clean_path}#L{line_no}"
                    findings["caching_fs_calls"].append({
                        "file": clean_path,
                        "line": line_no,
                        "protocol": proto,
                        "snippet": snippet,
                        "file_url": file_url,
                    })

                # 4. Cached class imports / references (BlockCacheFileSystem, WholeFileCacheFileSystem, DirFileSystem, etc.)
                for cls_name, desc in CACHE_CLASSES.items():
                    if cls_name in code:
                        for m in re.finditer(rf'\b{cls_name}\b', code):
                            line_no = code[:m.start()].count("\n") + 1
                            snippet = lines[line_no - 1].strip() if line_no <= len(lines) else ""
                            file_url = f"https://github.com/{repo_name}/blob/{successful_branch}/{clean_path}#L{line_no}"
                            findings["cached_class_refs"].append({
                                "file": clean_path,
                                "line": line_no,
                                "class": cls_name,
                                "description": desc,
                                "snippet": snippet,
                                "file_url": file_url,
                            })
                            break
    except Exception as e:
        print(f"[-] Error scanning {repo_name}: {e}", file=sys.stderr)

    return repo_name, findings


def generate_markdown_report(
    all_results: Dict[str, Dict[str, Any]], output_file: str
) -> str:
    """Generate comprehensive Markdown report detailing chained filesystem and cache usages."""
    total_repos = len(all_results)
    total_files = sum(r["total_files"] for r in all_results.values())
    repos_with_findings = [
        r
        for r in all_results.values()
        if r["chained_urls"]
        or r["cache_type_kwargs"]
        or r["caching_fs_calls"]
        or r["cached_class_refs"]
    ]

    def _slugify(text: str) -> str:
        return text.replace("/", "-").replace(".", "-").replace("_", "-").replace(" ", "-").lower()

    md: List[str] = [
        "# FSSPEC Chained Filesystems & Caching Layer Usage Report",
        "",
        f"- **Repositories Analyzed:** `{total_repos}`",
        f"- **Repositories with Chaining / Caching Findings:** `{len(repos_with_findings)}`",
        f"- **Total Files Scanned:** `{total_files}`",
        "",
        "---",
        "",
        "## 📊 Chained Filesystem & Cache Strategy Matrix",
        "",
        "| Repository | Total Findings | `simplecache::` | `filecache::` | `blockcache` | `DirFileSystem` | `ZipFileSystem` | Other Cache / Chaining |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    for r in all_results.values():
        name = r["repo_name"]
        repo_slug = _slugify(name)
        link = f"[{name}]({r['repo_url']})"

        # Count specific categories
        simplecache_cnt = sum(
            1 for u in r["chained_urls"] if u["protocol"] == "simplecache"
        ) + sum(1 for c in r["caching_fs_calls"] if c["protocol"] == "simplecache")

        filecache_cnt = sum(
            1 for u in r["chained_urls"] if u["protocol"] == "filecache"
        ) + sum(1 for c in r["caching_fs_calls"] if c["protocol"] == "filecache")

        blockcache_cnt = sum(
            1 for k in r["cache_type_kwargs"] if "block" in k["cache_type"]
        ) + sum(1 for u in r["chained_urls"] if "block" in u["protocol"])

        dirfs_cnt = sum(
            1 for c in r["cached_class_refs"] if c["class"] == "DirFileSystem"
        ) + sum(1 for f in r["caching_fs_calls"] if f["protocol"] == "dir")

        zipfs_cnt = sum(
            1 for c in r["cached_class_refs"] if c["class"] == "ZipFileSystem"
        ) + sum(1 for f in r["caching_fs_calls"] if f["protocol"] == "zip")

        other_cnt = (
            len(r["chained_urls"])
            + len(r["cache_type_kwargs"])
            + len(r["caching_fs_calls"])
            + len(r["cached_class_refs"])
            - (simplecache_cnt + filecache_cnt + blockcache_cnt + dirfs_cnt + zipfs_cnt)
        )

        total_findings = (
            len(r["chained_urls"])
            + len(r["cache_type_kwargs"])
            + len(r["caching_fs_calls"])
            + len(r["cached_class_refs"])
        )

        def _fmt(cnt: int, anchor_suffix: str) -> str:
            if cnt > 0:
                return f"[**{cnt}**](#{repo_slug}-{anchor_suffix})"
            return "-"

        md.append(
            f"| {link} | **{total_findings}** | {_fmt(simplecache_cnt, 'chained-urls')} | {_fmt(filecache_cnt, 'chained-urls')} | {_fmt(blockcache_cnt, 'blockcache')} | {_fmt(dirfs_cnt, 'dirfs')} | {_fmt(zipfs_cnt, 'zipfs')} | {str(other_cnt) if other_cnt > 0 else '-'} |"
        )

    md.extend([
        "",
        "---",
        "",
        "## 🔍 Detailed Chaining & Caching Findings by Repository",
        "",
    ])

    for r in repos_with_findings:
        name = r["repo_name"]
        repo_slug = _slugify(name)
        md.extend([
            f"### [{name}]({r['repo_url']})",
            "",
        ])

        # 1. Chained URLs
        if r["chained_urls"]:
            md.extend([
                f"#### <a id=\"{repo_slug}-chained-urls\"></a>🔹 Chained URL Patterns (`proto::target_url`) ({len(r['chained_urls'])} occurrences)",
                "",
                "<details open>",
                f"<summary><b>View {len(r['chained_urls'])} Chained URL Call Site(s) in {name}</b></summary>",
                "",
            ])
            for idx, item in enumerate(r["chained_urls"], start=1):
                md.extend([
                    f"##### {idx}. [{item['file']}]({item['file_url']}) (Line {item['line']})",
                    f"- **Protocol:** `{item['protocol']}::`",
                    f"- **Full Match:** `{item['match']}`",
                    "",
                    "```python",
                    f"{item['snippet']}",
                    "```",
                    "",
                ])
            md.extend(["</details>", ""])

        # 2. cache_type keywords
        if r["cache_type_kwargs"]:
            md.extend([
                f"#### <a id=\"{repo_slug}-blockcache\"></a>🔹 `cache_type` Configuration ({len(r['cache_type_kwargs'])} occurrences)",
                "",
                "<details open>",
                f"<summary><b>View {len(r['cache_type_kwargs'])} cache_type Usages in {name}</b></summary>",
                "",
            ])
            for idx, item in enumerate(r["cache_type_kwargs"], start=1):
                md.extend([
                    f"##### {idx}. [{item['file']}]({item['file_url']}) (Line {item['line']})",
                    f"- **Cache Strategy:** `{item['cache_type']}`",
                    "",
                    "```python",
                    f"{item['snippet']}",
                    "```",
                    "",
                ])
            md.extend(["</details>", ""])

        # 3. fsspec.filesystem caching/wrapper calls
        if r["caching_fs_calls"]:
            md.extend([
                f"#### <a id=\"{repo_slug}-caching-fs\"></a>🔹 Caching / Wrapper Filesystem Instantiations ({len(r['caching_fs_calls'])} occurrences)",
                "",
                "<details open>",
                f"<summary><b>View {len(r['caching_fs_calls'])} Filesystem Calls in {name}</b></summary>",
                "",
            ])
            for idx, item in enumerate(r["caching_fs_calls"], start=1):
                md.extend([
                    f"##### {idx}. [{item['file']}]({item['file_url']}) (Line {item['line']})",
                    f"- **Protocol:** `{item['protocol']}`",
                    "",
                    "```python",
                    f"{item['snippet']}",
                    "```",
                    "",
                ])
            md.extend(["</details>", ""])

        # 4. Cached class references
        if r["cached_class_refs"]:
            md.extend([
                f"#### <a id=\"{repo_slug}-cached-classes\"></a><a id=\"{repo_slug}-dirfs\"></a><a id=\"{repo_slug}-zipfs\"></a>🔹 Chained / Cached Class Implementations ({len(r['cached_class_refs'])} occurrences)",
                "",
                "<details open>",
                f"<summary><b>View {len(r['cached_class_refs'])} Class References in {name}</b></summary>",
                "",
            ])
            for idx, item in enumerate(r["cached_class_refs"], start=1):
                md.extend([
                    f"##### {idx}. [{item['file']}]({item['file_url']}) (Line {item['line']})",
                    f"- **Class:** `{item['class']}` ({item['description']})",
                    "",
                    "```python",
                    f"{item['snippet']}",
                    "```",
                    "",
                ])
            md.extend(["</details>", ""])

    out_p = Path(output_file)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    out_p.write_text("\n".join(md), encoding="utf-8")
    return str(out_p)


def main():
    parser = argparse.ArgumentParser(
        description="Scan repositories for fsspec chained filesystems and caching layers."
    )
    parser.add_argument(
        "--repo",
        "-r",
        nargs="+",
        help="One or more GitHub repositories to scan (e.g. intake/intake pydata/xarray).",
    )
    parser.add_argument(
        "-D",
        "--dependents-file",
        help="Path to dependents JSON file (default: data/default_dependents.json).",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="reports/chained_caching_report.md",
        help="Output Markdown report path (default: reports/chained_caching_report.md).",
    )
    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=16,
        help="Number of concurrent repository download/scan workers (default: 16).",
    )

    args = parser.parse_args()
    repos = load_repos(repo_file=args.dependents_file, explicit_repos=args.repo)

    if not repos:
        print("[-] No repositories found to scan.", file=sys.stderr)
        sys.exit(1)

    print(f"[+] Scanning {len(repos)} repositories for chained filesystems and caching layers...")
    results: Dict[str, Dict[str, Any]] = {}

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_map = {executor.submit(inspect_repository, r): r for r in repos}
        for future in as_completed(future_map):
            repo_name, res = future.result()
            results[repo_name] = res
            total_hits = (
                len(res["chained_urls"])
                + len(res["cache_type_kwargs"])
                + len(res["caching_fs_calls"])
                + len(res["cached_class_refs"])
            )
            print(f"    ✔ {repo_name:<35} | Scanned {res['total_files']} files | {total_hits} caching/chaining findings")

    out_file = generate_markdown_report(results, args.output)
    print(f"\n[+] Scan complete! Markdown report generated at: {out_file}")


if __name__ == "__main__":
    main()
