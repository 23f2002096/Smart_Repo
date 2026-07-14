from dataclasses import dataclass, field

from smart_repo.parser.models.call_info import CallInfo
from smart_repo.parser.models.class_info import ClassInfo
from smart_repo.parser.models.file_info import FileInfo
from smart_repo.parser.models.function_info import FunctionInfo
from smart_repo.parser.models.import_info import ImportInfo


@dataclass
class ParsedFile:
    """
    Complete parsed representation of one Python file.
    """

    file: FileInfo

    classes: list[ClassInfo] = field(default_factory=list)

    functions: list[FunctionInfo] = field(default_factory=list)

    imports: list[ImportInfo] = field(default_factory=list)

    calls: list[CallInfo] = field(default_factory=list)