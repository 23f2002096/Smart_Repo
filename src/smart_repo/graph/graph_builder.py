import networkx as nx

from smart_repo.parser.models import RepositoryInfo


class GraphBuilder:
    """
    Build a knowledge graph from a parsed repository.
    """

    def __init__(self):
        self.graph = nx.DiGraph()

    def build(self, repository: RepositoryInfo):

        for parsed_file in repository.files:

            file_node = parsed_file.file.relative_path

            self.graph.add_node(
                file_node,
                type="file",
            )

            # -------------------------
            # Functions
            # -------------------------

            for function in parsed_file.functions:

                function_node = function.name

                self.graph.add_node(
                    function_node,
                    type="function",
                )

                self.graph.add_edge(
                    file_node,
                    function_node,
                    relation="CONTAINS",
                )

            # -------------------------
            # Classes
            # -------------------------

            for cls in parsed_file.classes:

                class_node = cls.name

                self.graph.add_node(
                    class_node,
                    type="class",
                )

                self.graph.add_edge(
                    file_node,
                    class_node,
                    relation="CONTAINS",
                )

            # -------------------------
            # Imports
            # -------------------------

            for imp in parsed_file.imports:

                self.graph.add_node(
                    imp.module,
                    type="module",
                )

                self.graph.add_edge(
                    file_node,
                    imp.module,
                    relation="IMPORTS",
                )

            # -------------------------
            # Function Calls
            # -------------------------

            for call in parsed_file.calls:

                self.graph.add_node(
                    call.callee,
                    type="function",
                )

                self.graph.add_edge(
                    call.caller,
                    call.callee,
                    relation="CALLS",
                )

        return self.graph