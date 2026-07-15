from dataclasses import dataclass, field

from .call_info import CallInfo
from .class_info import ClassInfo
from .file_info import FileInfo
from .function_info import FunctionInfo
from .import_info import ImportInfo


@dataclass
class ParsedFile:
    """
    Represents one parsed Python source file.
    """

    file: FileInfo

    # NEW
    source_code: str = ""

    classes: list[ClassInfo] = field(default_factory=list)

    functions: list[FunctionInfo] = field(default_factory=list)

    imports: list[ImportInfo] = field(default_factory=list)

    calls: list[CallInfo] = field(default_factory=list)