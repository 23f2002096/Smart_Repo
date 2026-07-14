from pathlib import Path


IGNORED_FOLDERS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}


def scan_repository(repository_path: Path) -> list[dict]:
    """
    Scan repository and return metadata
    for every Python file.
    """

    python_files = []

    for path in repository_path.rglob("*.py"):

        if any(folder in path.parts for folder in IGNORED_FOLDERS):
            continue

        python_files.append(
            {
                "name": path.name,
                "path": str(path),
                "extension": path.suffix,
                "size": path.stat().st_size,
            }
        )

    return python_files