import ast
from pathlib import Path

from smart_repo.parser.models import (
    FileInfo,
    ParsedFile,
)
from smart_repo.parser.visitors import (
    CallVisitor,
    ClassVisitor,
    FunctionVisitor,
    ImportVisitor,
)


class ASTParser:
    """
    Parses a Python source file and extracts
    information using AST visitors.
    """

    def __init__(self, file_info: FileInfo):
        self.file_info = file_info

    def parse(self) -> ParsedFile:
        """
        Parse a Python source file and return a ParsedFile object.
        """

        # -----------------------------------
        # Read Source Code
        # -----------------------------------

        source = Path(
            self.file_info.absolute_path
        ).read_text(
            encoding="utf-8"
        )

        tree = ast.parse(source)

        # -----------------------------------
        # Parsed File
        # -----------------------------------

        parsed_file = ParsedFile(
            file=self.file_info,
            source_code=source,
        )

        # -----------------------------------
        # Import Visitor
        # -----------------------------------

        import_visitor = ImportVisitor()
        import_visitor.visit(tree)

        parsed_file.imports = import_visitor.imports

        # -----------------------------------
        # Function Visitor
        # -----------------------------------

        function_visitor = FunctionVisitor()
        function_visitor.visit(tree)

        parsed_file.functions = function_visitor.functions

        # -----------------------------------
        # Class Visitor
        # -----------------------------------

        class_visitor = ClassVisitor()
        class_visitor.visit(tree)

        parsed_file.classes = class_visitor.classes

        # -----------------------------------
        # Call Visitor
        # -----------------------------------

        call_visitor = CallVisitor()
        call_visitor.visit(tree)

        parsed_file.calls = call_visitor.calls

        return parsed_file