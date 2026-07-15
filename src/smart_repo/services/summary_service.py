from collections import Counter

from smart_repo.parser.models import RepositoryInfo


class RepositorySummaryService:
    """
    Generate a human-readable summary of a parsed repository.
    """

    def generate(self, repository: RepositoryInfo) -> str:

        total_files = len(repository.files)
        total_classes = 0
        total_functions = 0
        total_imports = 0
        total_calls = 0

        modules = Counter()
        imports = Counter()

        entry_point = "Unknown"

        for parsed_file in repository.files:

            file_path = parsed_file.file.relative_path

            # Detect entry point
            if file_path.endswith("app.py") or file_path.endswith("run.py"):
                entry_point = file_path

            total_classes += len(parsed_file.classes)
            total_functions += len(parsed_file.functions)
            total_imports += len(parsed_file.imports)
            total_calls += len(parsed_file.calls)

            # Top-level package/module
            parts = file_path.split("/")

            if len(parts) == 1:
                parts = file_path.split("\\")

            if len(parts) > 1:
                modules[parts[1] if len(parts) > 1 else parts[0]] += 1
            else:
                modules[parts[0]] += 1

            for imp in parsed_file.imports:
                root_module = imp.module.split(".")[0]
                imports[root_module] += 1

        summary = []

        summary.append("=" * 60)
        summary.append("SMART REPO SUMMARY")
        summary.append("=" * 60)
        summary.append("")
        summary.append(f"Repository : {repository.name}")
        summary.append("")
        summary.append("Statistics")
        summary.append(f"  Python Files   : {total_files}")
        summary.append(f"  Classes        : {total_classes}")
        summary.append(f"  Functions      : {total_functions}")
        summary.append(f"  Imports        : {total_imports}")
        summary.append(f"  Function Calls : {total_calls}")
        summary.append("")
        summary.append(f"Potential Entry Point : {entry_point}")
        summary.append("")

        summary.append("Top Packages")
        summary.append("------------------------------")

        if modules:
            for name, count in modules.most_common(10):
                summary.append(f"  • {name} ({count} files)")
        else:
            summary.append("  No packages found.")

        summary.append("")
        summary.append("Top Imported Modules")
        summary.append("------------------------------")

        if imports:
            for name, count in imports.most_common(10):
                summary.append(f"  • {name} ({count})")
        else:
            summary.append("  No imports found.")

        summary.append("")
        summary.append("Architecture")

        if any("flask" in module.lower() for module in imports):
            summary.append("  • Flask Web Application")

        if any("networkx" in module.lower() for module in imports):
            summary.append("  • NetworkX Knowledge Graph")

        if any("sqlite" in module.lower() for module in imports):
            summary.append("  • SQLite Database")

        if any("fastapi" in module.lower() for module in imports):
            summary.append("  • FastAPI Backend")

        summary.append("")
        summary.append("=" * 60)

        return "\n".join(summary)