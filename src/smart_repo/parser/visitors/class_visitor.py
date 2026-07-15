import ast

from smart_repo.parser.models import ClassInfo


class ClassVisitor(ast.NodeVisitor):
    """
    Extract all class definitions from a Python file.
    """

    def __init__(self):
        self.classes: list[ClassInfo] = []

    def visit_ClassDef(self, node: ast.ClassDef):

        class_info = ClassInfo(
            name=node.name,
            line_number=node.lineno,
            end_line=getattr(node, "end_lineno", node.lineno),
            base_classes=[
                ast.unparse(base)
                for base in node.bases
            ],
        )

        self.classes.append(class_info)

        self.generic_visit(node)