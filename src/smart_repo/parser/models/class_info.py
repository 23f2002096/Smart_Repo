from dataclasses import dataclass, field

from smart_repo.parser.models.function_info import FunctionInfo


@dataclass
class ClassInfo:
    """
    Information about a class.
    """

    name: str
    line_number: int
    base_classes: list[str] = field(default_factory=list)
    methods: list[FunctionInfo] = field(default_factory=list)