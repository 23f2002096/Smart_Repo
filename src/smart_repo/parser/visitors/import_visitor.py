import ast

from smart_repo.parser.models import ImportInfo


class ImportVisitor(ast.NodeVisitor):
    """
    Extract all import statements from a Python file.
    """

    def __init__(self):
        self.imports: list[ImportInfo] = []

    def visit_Import(self, node: ast.Import):

        for alias in node.names:
            self.imports.append(
                ImportInfo(
                    module=alias.name,
                    alias=alias.asname,
                )
            )

        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.Import):

        module = node.module or ""

        for alias in node.names:
            self.imports.append(
                ImportInfo(
                    module=f"{module}.{alias.name}",
                    alias=alias.asname,
                )
            )

        self.generic_visit(node)