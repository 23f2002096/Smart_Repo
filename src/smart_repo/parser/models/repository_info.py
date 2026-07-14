from dataclasses import dataclass, field

from smart_repo.parser.models import ParsedFile


@dataclass
class RepositoryInfo:
    """
    Complete parsed repository.
    """

    name: str

    files: list[ParsedFile] = field(default_factory=list)