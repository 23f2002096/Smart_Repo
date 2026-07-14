from smart_repo.graph.models import (
    GraphData,
    GraphEdge,
    GraphNode,
)


class GraphConverter:

    def convert(self, repository):

        graph = GraphData()

        repository_node = GraphNode(
            id=repository.name,
            label=repository.name,
            node_type="repository",
        )

        graph.nodes.append(repository_node)

        for parsed_file in repository.files:

            file_id = parsed_file.file.relative_path

            graph.nodes.append(
                GraphNode(
                    id=file_id,
                    label=parsed_file.file.name,
                    node_type="file",
                )
            )

            graph.edges.append(
                GraphEdge(
                    source=repository.name,
                    target=file_id,
                    relationship="CONTAINS",
                )
            )

            # Functions
            for function in parsed_file.functions:

                function_id = (
                    f"{file_id}::{function.name}"
                )

                graph.nodes.append(
                    GraphNode(
                        id=function_id,
                        label=function.name,
                        node_type="function",
                    )
                )

                graph.edges.append(
                    GraphEdge(
                        source=file_id,
                        target=function_id,
                        relationship="CONTAINS",
                    )
                )

            # Classes
            for cls in parsed_file.classes:

                class_id = (
                    f"{file_id}::{cls.name}"
                )

                graph.nodes.append(
                    GraphNode(
                        id=class_id,
                        label=cls.name,
                        node_type="class",
                    )
                )

                graph.edges.append(
                    GraphEdge(
                        source=file_id,
                        target=class_id,
                        relationship="CONTAINS",
                    )
                )

        return graph