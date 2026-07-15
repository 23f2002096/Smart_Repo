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
            end_line=getattr(node, "end_lineno", node.lineno),
            arguments=[
                arg.arg
                for arg in node.args.args
            ],
            decorators=[
                ast.unparse(d)
                for d in node.decorator_list
            ],
        )

        self.functions.append(function)

        self.generic_visit(node)