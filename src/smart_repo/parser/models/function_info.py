from dataclasses import dataclass, field


@dataclass
class FunctionInfo:
    """
    Stores information about a function.
    """

    name: str

    line_number: int

    end_line: int

    arguments: list[str] = field(default_factory=list)

    decorators: list[str] = field(default_factory=list)