from dataclasses import dataclass, field


@dataclass
class FunctionInfo:
    """
    Information about a function.
    """

    name: str
    line_number: int
    arguments: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)