from pathlib import Path

from smart_repo.parser.ast_parser import ASTParser
from smart_repo.parser.models import (
    FileInfo,
    RepositoryInfo,
)
from smart_repo.parser.scanner import RepositoryScanner


class RepositoryParser:
    """
    Parse an entire repository.
    """

    def __init__(self, repository_path: Path):

        self.repository_path = Path(repository_path)

    def parse(self) -> RepositoryInfo:

        scanner = RepositoryScanner(
            self.repository_path
        )

        python_files = scanner.scan()

        repository = RepositoryInfo(
            name=self.repository_path.name
        )

        for file in python_files:

            parser = ASTParser(file)

            parsed = parser.parse()

            repository.files.append(parsed)

        return repository