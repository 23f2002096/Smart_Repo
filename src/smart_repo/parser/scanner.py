from pathlib import Path

IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode",
    "env",
    "venv",
}


class RepositoryScanner:
    """
    Scans a repository and collects metadata
    for all Python source files.
    """

    def __init__(self, repository_path: Path):
        self.repository_path = Path(repository_path)

    def scan(self) -> list[dict]:
        python_files = []

        for file_path in self.repository_path.rglob("*.py"):

            if any(folder in file_path.parts for folder in IGNORED_DIRECTORIES):
                continue

            python_files.append(
                {
                    "name": file_path.name,
                    "path": str(file_path.relative_to(self.repository_path)),
                    "absolute_path": str(file_path),
                    "extension": file_path.suffix,
                    "size": file_path.stat().st_size,
                }
            )

        python_files.sort(key=lambda x: x["path"])

        return python_files