import networkx as nx

from smart_repo.parser.models import RepositoryInfo

STANDARD_MODULES = {
    "os",
    "sys",
    "json",
    "typing",
    "pathlib",
    "collections",
    "dataclasses",
    "logging",
    "math",
    "re",
    "itertools",
    "time",
    "copy",
    "functools",
    "datetime",
}

class GraphBuilder:
    """
    Build a directed knowledge graph from a parsed repository.

    Node Types:
        - file
        - class
        - function
        - module

    Edge Types:
        - CONTAINS
        - IMPORTS
        - CALLS
    """

    def __init__(self):
        self.graph = nx.DiGraph()

    def build(self, repository: RepositoryInfo):

        self.graph.clear()

        for parsed_file in repository.files:

            # =====================================================
            # File Node
            # =====================================================

            file_node = parsed_file.file.relative_path

            self.graph.add_node(
                file_node,
                type="file",
                label=parsed_file.file.name,
                path=parsed_file.file.relative_path,
            )

            # =====================================================
            # Function Nodes
            # =====================================================

            for function in parsed_file.functions:

                function_node = (
                    f"{file_node}:{function.name}"
                )

                self.graph.add_node(
                    function_node,
                    type="function",
                    label=function.name,
                    file=file_node,
                    line=function.line_number,
                )

                self.graph.add_edge(
                    file_node,
                    function_node,
                    relation="CONTAINS",
                )

            # =====================================================
            # Class Nodes
            # =====================================================

            for cls in parsed_file.classes:

                class_node = (
                    f"{file_node}:{cls.name}"
                )

                self.graph.add_node(
                    class_node,
                    type="class",
                    label=cls.name,
                    file=file_node,
                    line=cls.line_number,
                )

                self.graph.add_edge(
                    file_node,
                    class_node,
                    relation="CONTAINS",
                )

            # =====================================================
            # Import Nodes
            # =====================================================

            for imp in parsed_file.imports:

                root_module = imp.module.split(".")[0]

                if root_module in STANDARD_MODULES:
                    continue

                module_node = imp.module

                self.graph.add_node(
                    module_node,
                    type="module",
                    label=module_node.split(".")[-1],
                )

                self.graph.add_edge(
                    file_node,
                    module_node,
                    relation="IMPORTS",
                )

            # =====================================================
            # Function Call Nodes
            # =====================================================

            for call in parsed_file.calls:

                caller_node = (
                    f"{file_node}:{call.caller}"
                )

                callee_node = call.callee

                # If the callee doesn't exist yet,
                # create it as an external function.

                if not self.graph.has_node(callee_node):

                    self.graph.add_node(
                        callee_node,
                        type="function",
                        label=callee_node.split(".")[-1],
                    )

                # Ensure caller exists
                if not self.graph.has_node(caller_node):

                    self.graph.add_node(
                        caller_node,
                        type="function",
                        label=call.caller,
                        file=file_node,
                    )

                self.graph.add_edge(
                    caller_node,
                    callee_node,
                    relation="CALLS",
                )

        return self.graph