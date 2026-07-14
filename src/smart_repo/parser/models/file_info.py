from dataclasses import dataclass


@dataclass
class FileInfo:
    """
    Metadata about a Python source file.
    """

    name: str
    relative_path: str
    absolute_path: str
    extension: str
    size: int