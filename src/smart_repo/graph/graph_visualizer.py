from pathlib import Path

from pyvis.network import Network


class GraphVisualizer:
    """
    Visualize a NetworkX graph using PyVis.
    """

    def __init__(self, graph):
        self.graph = graph

    def visualize(self, output_file: str = "knowledge_graph.html") -> Path:

        net = Network(
            height="800px",
            width="100%",
            directed=True,
        )

        net.from_nx(self.graph)

        net.toggle_physics(True)

        # IMPORTANT
        net.write_html(
            output_file,
            notebook=False,
            open_browser=False,
        )

        return Path(output_file)