import ast

from smart_repo.parser.models import CallInfo


class CallVisitor(ast.NodeVisitor):
    """
    Extract function calls from a Python file.
    """

    def __init__(self):
        self.calls: list[CallInfo] = []
        self.current_function = None

    def visit_FunctionDef(self, node: ast.FunctionDef):

        previous_function = self.current_function
        self.current_function = node.name

        self.generic_visit(node)

        self.current_function = previous_function

    def visit_Call(self, node: ast.Call):

        if self.current_function:

            try:
                callee = ast.unparse(node.func)
            except Exception:
                callee = "unknown"

            self.calls.append(
                CallInfo(
                    caller=self.current_function,
                    callee=callee,
                    line_number=node.lineno,
                )
            )

        self.generic_visit(node)