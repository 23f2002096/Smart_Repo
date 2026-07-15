from dataclasses import dataclass, field


@dataclass
class ClassInfo:
    """
    Stores information about a class.
    """

    name: str

    line_number: int

    end_line: int

    base_classes: list[str] = field(default_factory=list)