import ast

from smart_repo.parser.models import FunctionInfo


class FunctionVisitor(ast.NodeVisitor):
    """
    Extract all function definitions from a Python file.
    """

    def __init__(self):
        self.functions: list[FunctionInfo] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):

        function = FunctionInfo(
            name=node.name,
            line_number=node.lineno,
            arguments=[arg.arg for arg in node.args.args],
            decorators=[
                ast.unparse(decorator)
                for decorator in node.decorator_list
            ],
        )

        self.functions.append(function)

        self.generic_visit(node)