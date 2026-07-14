from dataclasses import dataclass


@dataclass
class ImportInfo:
    """
    Information about an import statement.
    """

    module: str
    alias: str | None = None