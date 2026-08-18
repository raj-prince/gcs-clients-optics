"""
Use Case 4: Storage Protocols & Cloud Backend Driver Usage Analysis.
"""

import ast
import csv
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from gcs_clients_optics.usecases.base import BaseUseCase

PROTOCOL_PATTERNS: Dict[str, str] = {
    "gs": "Google Cloud Storage (`gs://`)",
    "gcs": "Google Cloud Storage (`gcs://`)",
    "s3": "Amazon S3 (`s3://`)",
    "s3a": "Amazon S3A (`s3a://`)",
    "abfs": "Azure Blob Storage (`abfs://`)",
    "abfss": "Azure Data Lake Gen2 (`abfss://`)",
    "az": "Azure Storage (`az://`)",
    "hdfs": "Hadoop Distributed FS (`hdfs://`)",
    "memory": "In-Memory Filesystem (`memory://`)",
    "file": "Local Disk (`file://`)",
    "http": "HTTP Remote Stream (`http://`)",
    "https": "HTTPS Secure Remote Stream (`https://`)",
    "sftp": "SFTP Protocol (`sftp://`)",
    "zip": "Zip Archive Chained (`zip://`)",
    "tar": "Tar Archive Chained (`tar://`)",
    "github": "GitHub Raw Protocol (`github://`)",
}

URI_REGEX = re.compile(
    r"\b(gs|gcs|s3|s3a|abfs|abfss|az|hdfs|memory|file|https?|sftp|zip|tar|github)://[^\s\"'>]+"
)


@dataclass
class ProtocolUsageItem:
    """Represents a detected storage protocol or cloud backend usage."""

    file_path: str
    line_number: int
    protocol: str
    provider: str
    usage_type: str  # "uri_string" or "driver_instantiation"
    context: str
    repo_url: Optional[str] = None
    file_url: Optional[str] = None
    code_snippet: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProtocolReport:
    """Aggregated protocol usage report for a repository or target."""

    target_source: str
    total_files_scanned: int
    files_with_protocols: int
    total_protocol_usages: int
    protocol_counts: Dict[str, int] = field(default_factory=dict)
    provider_counts: Dict[str, int] = field(default_factory=dict)
    repo_url: Optional[str] = None
    items: List[ProtocolUsageItem] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["items"] = [i.to_dict() for i in self.items]
        return data


class ProtocolASTVisitor(ast.NodeVisitor):
    """AST visitor to find protocol URIs and filesystem driver instantiations."""

    def __init__(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ):
        self.file_path = file_path
        self.source_lines = source_code.splitlines()
        self.repo_url = repo_url
        self.branch = branch
        self.usages: List[ProtocolUsageItem] = []

    def _get_provider(self, proto: str) -> str:
        p = proto.lower()
        if p in ("gs", "gcs", "gcsfs"):
            return "Google Cloud Storage (GCS)"
        elif p in ("s3", "s3a", "s3fs"):
            return "Amazon Web Services (S3)"
        elif p in ("abfs", "abfss", "az", "adl", "adlfs"):
            return "Microsoft Azure (Blob/ADLS)"
        elif p in ("hdfs",):
            return "Hadoop HDFS"
        elif p in ("memory",):
            return "In-Memory Storage"
        elif p in ("file", "local"):
            return "Local Filesystem"
        elif p in ("http", "https"):
            return "Web / HTTP"
        else:
            return "Other / Chained Protocol"

    def _build_url(self, line: int) -> Optional[str]:
        if self.repo_url:
            return f"{self.repo_url.rstrip('/')}/blob/{self.branch}/{self.file_path}#L{line}"
        return f"file://{Path(self.file_path).resolve()}#L{line}"

    def visit_Constant(self, node: ast.Constant):
        if isinstance(node.value, str):
            for match in URI_REGEX.finditer(node.value):
                proto = match.group(1).lower()
                provider = self._get_provider(proto)
                line = getattr(node, "lineno", 1)
                snippet = (
                    self.source_lines[line - 1].strip()
                    if 0 < line <= len(self.source_lines)
                    else node.value
                )
                self.usages.append(
                    ProtocolUsageItem(
                        file_path=self.file_path,
                        line_number=line,
                        protocol=proto,
                        provider=provider,
                        usage_type="uri_string",
                        context=match.group(0)[:60],
                        repo_url=self.repo_url,
                        file_url=self._build_url(line),
                        code_snippet=snippet,
                    )
                )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        # Detect fsspec.filesystem("gcs" / "s3" / "abfs") or GCSFileSystem()
        proto_detected = None
        if isinstance(node.func, ast.Attribute) and node.func.attr == "filesystem":
            if node.args and isinstance(node.args[0], ast.Constant):
                proto_detected = str(node.args[0].value).lower()
        elif isinstance(node.func, ast.Attribute) and node.func.attr in (
            "GCSFileSystem",
            "S3FileSystem",
            "AzureBlobFileSystem",
        ):
            proto_detected = node.func.attr.replace("FileSystem", "").lower()
        elif isinstance(node.func, ast.Name) and node.func.id in (
            "GCSFileSystem",
            "S3FileSystem",
            "AzureBlobFileSystem",
        ):
            proto_detected = node.func.id.replace("FileSystem", "").lower()

        if proto_detected:
            line = node.lineno
            provider = self._get_provider(proto_detected)
            snippet = (
                self.source_lines[line - 1].strip()
                if 0 < line <= len(self.source_lines)
                else ""
            )
            self.usages.append(
                ProtocolUsageItem(
                    file_path=self.file_path,
                    line_number=line,
                    protocol=proto_detected,
                    provider=provider,
                    usage_type="driver_instantiation",
                    context=f"driver: {proto_detected}",
                    repo_url=self.repo_url,
                    file_url=self._build_url(line),
                    code_snippet=snippet,
                )
            )

        self.generic_visit(node)


class ProtocolsUseCase(BaseUseCase):
    """
    Analyzes cloud storage protocol URIs and backend driver usage across codebases.
    """

    name = "protocols"
    description = (
        "Analyze storage protocol URIs (gs://, s3://, abfs://) and backend driver usage."
    )
    aliases = ["storage", "backends", "cloud-providers"]

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[ProtocolUsageItem]:
        """Scan code for protocol URIs and driver instantiations."""
        try:
            tree = ast.parse(source_code, filename=file_path)
            visitor = ProtocolASTVisitor(
                file_path, source_code, repo_url=repo_url, branch=branch
            )
            visitor.visit(tree)
            return visitor.usages
        except Exception:
            return []

    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[ProtocolUsageItem],
        repo_url: Optional[str] = None,
    ) -> ProtocolReport:
        """Aggregate protocol usages into a ProtocolReport."""
        proto_counts: Dict[str, int] = {}
        provider_counts: Dict[str, int] = {}

        for item in usages:
            proto_counts[item.protocol] = proto_counts.get(item.protocol, 0) + 1
            provider_counts[item.provider] = (
                provider_counts.get(item.provider, 0) + 1
            )

        return ProtocolReport(
            target_source=target_source,
            total_files_scanned=total_files_scanned,
            files_with_protocols=files_with_usages,
            total_protocol_usages=len(usages),
            protocol_counts=proto_counts,
            provider_counts=provider_counts,
            repo_url=repo_url,
            items=usages,
        )

    def export_reports(
        self,
        reports: List[ProtocolReport],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        output_sqlite: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, str]:
        """Export protocol analysis in CSV, JSON, Markdown, and SQLite formats."""
        generated: Dict[str, str] = {}

        if output_sqlite:
            from gcs_clients_optics.storage.sqlite_store import ingest_protocol_reports
            ingest_protocol_reports(
                reports,
                output_sqlite,
                elapsed_seconds=kwargs.get("elapsed_seconds", 0.0),
            )
            generated["sqlite"] = output_sqlite

        if output_csv:
            self._export_csv(reports, output_csv)
            generated["csv"] = output_csv

        if output_json:
            self._export_json(reports, output_json, kwargs.get("elapsed_seconds", 0.0))
            generated["json"] = output_json

        if output_md:
            self._export_markdown(reports, output_md)
            generated["markdown"] = output_md

        return generated

    def _export_csv(self, reports: List[ProtocolReport], output_path: str):
        rows = []
        for r in reports:
            repo_name = (
                r.target_source.replace("GitHub:", "")
                .replace("Local:", "")
                .split()[0]
            )
            for item in r.items:
                rows.append([
                    repo_name,
                    item.file_path,
                    item.line_number,
                    item.protocol,
                    item.provider,
                    item.usage_type,
                    item.context,
                    item.file_url or "",
                    item.code_snippet.replace("\n", " "),
                ])

        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "repository",
                "file_path",
                "line_number",
                "protocol",
                "provider",
                "usage_type",
                "context",
                "file_url",
                "code_snippet",
            ])
            writer.writerows(rows)

    def _export_json(
        self, reports: List[ProtocolReport], output_path: str, elapsed_seconds: float
    ):
        global_proto: Dict[str, int] = {}
        global_prov: Dict[str, int] = {}
        for r in reports:
            for k, v in r.protocol_counts.items():
                global_proto[k] = global_proto.get(k, 0) + v
            for k, v in r.provider_counts.items():
                global_prov[k] = global_prov.get(k, 0) + v

        json_data = {
            "summary": {
                "total_targets": len(reports),
                "total_files_scanned": sum(r.total_files_scanned for r in reports),
                "total_protocol_usages": sum(
                    r.total_protocol_usages for r in reports
                ),
                "protocol_counts": global_proto,
                "provider_counts": global_prov,
                "elapsed_seconds": round(elapsed_seconds, 2),
            },
            "per_repository": [r.to_dict() for r in reports],
        }

        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(json_data, indent=2), encoding="utf-8")

    def _export_markdown(self, reports: List[ProtocolReport], output_path: str):
        total_files = sum(r.total_files_scanned for r in reports)
        total_usages = sum(r.total_protocol_usages for r in reports)

        global_proto: Dict[str, int] = {}
        global_prov: Dict[str, int] = {}
        for r in reports:
            for k, v in r.protocol_counts.items():
                global_proto[k] = global_proto.get(k, 0) + v
            for k, v in r.provider_counts.items():
                global_prov[k] = global_prov.get(k, 0) + v

        lines = [
            "# Storage Protocols & Cloud Backend Optics Report",
            "",
            "This report analyzes **storage protocols (`gs://`, `s3://`, `abfs://`, etc.) and backend filesystem drivers** across open-source codebases.",
            "",
            "---",
            "",
            "## 📊 Global Cloud Provider Breakdown",
            "",
            f"- **Repositories/Targets Scanned:** `{len(reports)}`",
            f"- **Total Files Scanned:** `{total_files}`",
            f"- **Total Protocol Usages Detected:** `{total_usages}`",
            "",
            "| Cloud Provider / Backend | Total Usages | % Share |",
            "| :--- | :---: | :---: |",
        ]

        for prov, cnt in sorted(global_prov.items(), key=lambda x: -x[1]):
            pct = (cnt / total_usages * 100) if total_usages else 0.0
            lines.append(f"| **{prov}** | **{cnt}** | `{pct:.1f}%` |")

        lines.extend([
            "",
            "---",
            "",
            "## 📈 Protocol URI Scheme Breakdown",
            "",
            "| Protocol Scheme | Occurrences | % Share | Description |",
            "| :--- | :---: | :---: | :--- |",
        ])

        for proto, cnt in sorted(global_proto.items(), key=lambda x: -x[1]):
            pct = (cnt / total_usages * 100) if total_usages else 0.0
            desc = PROTOCOL_PATTERNS.get(proto, f"Custom protocol ({proto}://)")
            lines.append(f"| **`{proto}`** | **{cnt}** | `{pct:.1f}%` | {desc} |")

        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(lines), encoding="utf-8")

    def print_summary(self, reports: List[ProtocolReport]) -> None:
        """Print console overview."""
        total_usages = sum(r.total_protocol_usages for r in reports)
        print("\n" + "=" * 70)
        print("  🌐 STORAGE PROTOCOLS & CLOUD BACKENDS SUMMARY")
        print("=" * 70)
        print(f"  • Targets Scanned:         {len(reports)}")
        print(f"  • Total Protocol Matches:  {total_usages}")
        print("=" * 70)
