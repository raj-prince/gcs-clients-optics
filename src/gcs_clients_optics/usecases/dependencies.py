"""
Use Case 7: Dependency Versions Analysis (fsspec / gcsfs / cloud storage packages).

Extracts and audits package version constraints for fsspec, gcsfs, s3fs, adlfs, and pyarrow
across repository manifests (pyproject.toml, requirements.txt, setup.py, setup.cfg, environment.yml).
"""

import csv
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from gcs_clients_optics.usecases.base import BaseUseCase

TARGET_PACKAGES: Set[str] = {
    "fsspec",
    "gcsfs",
    "s3fs",
    "adlfs",
    "pyarrow",
    "google-cloud-storage",
    "abfs",
}

MANIFEST_PATTERNS: Set[str] = {
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "environment.yml",
    "environment.yaml",
    "Pipfile",
}


@dataclass
class DependencyVersionItem:
    """Represents a detected dependency version constraint."""

    package_name: str
    specifier: str
    constraint_type: str  # pinned, minimum, range, compatible, unconstrained
    manifest_path: str
    line_number: int
    raw_entry: str
    file_url: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DependencyReport:
    """Target-level aggregate report for package dependency versions."""

    target_source: str
    total_files_scanned: int
    files_with_usages: int
    total_dependencies_found: int
    items: List[DependencyVersionItem] = field(default_factory=list)
    package_summary: Dict[str, List[str]] = field(default_factory=dict)
    repo_url: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["items"] = [i.to_dict() for i in self.items]
        return d


def parse_dependency_line(line: str, manifest_path: str, line_number: int) -> Optional[DependencyVersionItem]:
    """Parse a single line from a requirement/manifest file looking for target packages."""
    clean = line.strip()
    if not clean or clean.startswith("#") or clean.startswith("//"):
        return None

    # Strip inline comments
    clean = clean.split("#")[0].strip()

    # Regex matching: package_name [extras] (operator version)?
    for pkg in TARGET_PACKAGES:
        # Match e.g. "fsspec>=2023.1.0", "fsspec[gcs]~=2024.2", "gcsfs==2023.9.2", "fsspec"
        pattern = rf'^\s*["\']?({re.escape(pkg)}(?:\[[^\]]+\])?)\s*([<>=~!^].*?)?["\']?,?\s*$'
        match = re.search(pattern, clean, re.IGNORECASE)
        if not match:
            # Also try substring match in pyproject/setup lists: e.g. "fsspec >= 2023.1.0"
            sub_pattern = rf'["\']({re.escape(pkg)}(?:\[[^\]]+\])?)\s*([<>=~!^][^"\']*)?["\']'
            match = re.search(sub_pattern, clean, re.IGNORECASE)

        if match:
            pkg_matched = match.group(1).strip()
            raw_spec = match.group(2).strip() if match.group(2) else ""
            spec = raw_spec.rstrip('",\'') if raw_spec else "*"

            # Classify constraint type
            if spec == "*":
                c_type = "unconstrained"
            elif "==" in spec or "===" in spec:
                c_type = "pinned"
            elif "~=" in spec or "^" in spec:
                c_type = "compatible"
            elif ">=" in spec and "<" in spec:
                c_type = "range"
            elif ">=" in spec:
                c_type = "minimum"
            elif "<=" in spec or "<" in spec:
                c_type = "maximum"
            else:
                c_type = "custom"

            base_pkg = pkg_matched.split("[")[0].lower()
            return DependencyVersionItem(
                package_name=base_pkg,
                specifier=spec if spec else "*",
                constraint_type=c_type,
                manifest_path=manifest_path,
                line_number=line_number,
                raw_entry=clean,
            )

    return None


class DependencyVersionsUseCase(BaseUseCase):
    """
    Use Case 7: Dependency Versions Analysis.
    Scans repository manifests to extract fsspec, gcsfs, and storage package versions.
    """

    name = "dependencies"
    description = "Audit fsspec & gcsfs package version constraints in repository manifests"
    aliases = ["versions", "deps", "package-versions"]

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[DependencyVersionItem]:
        items: List[DependencyVersionItem] = []
        p = Path(file_path)
        fn = p.name.lower()

        # Check if file is a manifest
        is_manifest = False
        if fn in MANIFEST_PATTERNS or fn.startswith("requirements") or fn.endswith((".toml", ".yml", ".yaml")):
            is_manifest = True
        elif fn.endswith(".py") and fn in ("setup.py", "version.py", "_version.py", "__init__.py"):
            is_manifest = True

        if not is_manifest:
            return []

        lines = source_code.splitlines()
        for idx, line in enumerate(lines, 1):
            item = parse_dependency_line(line, file_path, idx)
            if item:
                if repo_url:
                    clean_url = repo_url.rstrip("/")
                    item.file_url = f"{clean_url}/blob/{branch}/{file_path}#L{idx}"
                items.append(item)

        return items

    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[DependencyVersionItem],
        repo_url: Optional[str] = None,
    ) -> DependencyReport:
        pkg_summary: Dict[str, List[str]] = {}
        for u in usages:
            pkg_summary.setdefault(u.package_name, []).append(u.specifier)

        return DependencyReport(
            target_source=target_source,
            total_files_scanned=total_files_scanned,
            files_with_usages=files_with_usages,
            total_dependencies_found=len(usages),
            items=usages,
            package_summary=pkg_summary,
            repo_url=repo_url,
        )

    def export_reports(
        self,
        reports: List[DependencyReport],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        output_sqlite: Optional[str] = None,
        elapsed_seconds: float = 0.0,
        **kwargs,
    ) -> Dict[str, str]:
        results = {}

        if output_csv:
            p = Path(output_csv)
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Target",
                    "Package Name",
                    "Version Specifier",
                    "Constraint Type",
                    "Manifest File",
                    "Line",
                    "Raw Entry",
                    "File URL",
                ])
                for r in reports:
                    for item in r.items:
                        writer.writerow([
                            r.target_source,
                            item.package_name,
                            item.specifier,
                            item.constraint_type,
                            item.manifest_path,
                            item.line_number,
                            item.raw_entry,
                            item.file_url or "",
                        ])
            results["csv"] = str(p)

        if output_json:
            p = Path(output_json)
            p.parent.mkdir(parents=True, exist_ok=True)
            data = {
                "total_targets": len(reports),
                "total_dependencies": sum(r.total_dependencies_found for r in reports),
                "elapsed_seconds": elapsed_seconds,
                "targets": [r.to_dict() for r in reports],
            }
            with open(p, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            results["json"] = str(p)

        if output_md:
            p = Path(output_md)
            p.parent.mkdir(parents=True, exist_ok=True)
            total_deps = sum(r.total_dependencies_found for r in reports)

            lines = [
                "# 📦 Downstream Dependency Versions Analysis Report",
                "",
                f"Evaluated package manifests across **{len(reports)}** repository targets in **{elapsed_seconds:.2f}s**.",
                "",
                "## 📊 Executive Summary",
                "",
                f"- **Total Storage Package Constraints Found**: `{total_deps}`",
                "",
                "## 📋 Repository Storage Package Version Matrix",
                "",
                "| Repository | `fsspec` Version | `gcsfs` Version | `s3fs` Version | `adlfs` Version | `pyarrow` Version |",
                "| :--- | :--- | :--- | :--- | :--- | :--- |",
            ]
            for r in reports:
                fsspec_ver = ", ".join(r.package_summary.get("fsspec", ["—"]))
                gcsfs_ver = ", ".join(r.package_summary.get("gcsfs", ["—"]))
                s3fs_ver = ", ".join(r.package_summary.get("s3fs", ["—"]))
                adlfs_ver = ", ".join(r.package_summary.get("adlfs", ["—"]))
                pyarrow_ver = ", ".join(r.package_summary.get("pyarrow", ["—"]))
                lines.append(
                    f"| **`{r.target_source}`** | `{fsspec_ver}` | `{gcsfs_ver}` | `{s3fs_ver}` | `{adlfs_ver}` | `{pyarrow_ver}` |"
                )

            lines.extend([
                "",
                "## 🔍 Detailed Manifest Entries",
                "",
            ])
            for r in reports:
                if r.items:
                    lines.append(f"### `{r.target_source}`")
                    for item in r.items:
                        lines.append(
                            f"- **{item.package_name}** `{item.specifier}` ({item.constraint_type}) in `{item.manifest_path}:{item.line_number}`"
                        )
                        lines.append(f"  `{item.raw_entry}`")
                    lines.append("")

            with open(p, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            results["md"] = str(p)

        if output_sqlite:
            from gcs_clients_optics.storage.sqlite_store import ingest_dependency_reports
            ingest_dependency_reports(reports, output_sqlite, elapsed_seconds=elapsed_seconds)
            results["sqlite"] = output_sqlite

        return results

    def print_summary(self, reports: List[DependencyReport]) -> None:
        total_deps = sum(r.total_dependencies_found for r in reports)
        print("\n" + "=" * 70)
        print("  📦 DEPENDENCY VERSIONS USAGE SUMMARY")
        print("=" * 70)
        print(f"  • Total Targets Scanned:              {len(reports)}")
        print(f"  • Total Storage Package Constraints:  {total_deps}")
        print("=" * 70)
