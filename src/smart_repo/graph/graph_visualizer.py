from pathlib import Path

from pyvis.network import Network


class GraphVisualizer:
    """
    Generate an interactive knowledge graph using PyVis.
    """

    NODE_STYLES = {
        "file": {
            "color": "#2563EB",
            "shape": "box",
            "size": 40,
        },
        "class": {
            "color": "#10B981",
            "shape": "ellipse",
            "size": 28,
        },
        "function": {
            "color": "#F59E0B",
            "shape": "dot",
            "size": 14,
        },
        "module": {
            "color": "#EF4444",
            "shape": "diamond",
            "size": 20,
        },
    }

    EDGE_COLORS = {
        "CONTAINS": "#2563EB",
        "IMPORTS": "#DC2626",
        "CALLS": "#059669",
    }

    def __init__(self, graph):
        self.graph = graph

    def visualize(self, output_file: str = "knowledge_graph.html") -> Path:

        net = Network(
            height="900px",
            width="100%",
            directed=True,
            bgcolor="#FFFFFF",
            font_color="black",
        )
        net.set_options("""
            var options = {
                "physics": {
                    "enabled": true,
                    "barnesHut": {
                    "gravitationalConstant": -25000,
                    "springLength": 180,
                    "springConstant": 0.03,
                    "damping": 0.09
                    },
                    "stabilization": {
                    "iterations": 200
                    }
                },
                "interaction": {
                    "hover": true,
                    "navigationButtons": true,
                    "keyboard": true
                },
                "edges": {
                    "smooth": {
                    "type": "dynamic"
                    }
                }
            }
        """)

        # ---------------------------------------------------
        # Nodes
        # ---------------------------------------------------

        for node, attrs in self.graph.nodes(data=True):

            node_type = attrs.get("type", "file")

            style = self.NODE_STYLES.get(
                node_type,
                self.NODE_STYLES["file"],
            )

            net.add_node(
                node,
                label=attrs.get("label", node),
                title=f"""
                    <b>{attrs.get('label', node)}</b>

                    <hr>

                    <b>Type</b> : {node_type}

                    <b>File</b> : {attrs.get('file', '-')}

                    <b>Line</b> : {attrs.get('line', '-')}

                    <b>ID</b> : {node}
                """,
                color=style["color"],
                shape=style["shape"],
                size=style["size"],
            )

        # ---------------------------------------------------
        # Edges
        # ---------------------------------------------------

        for source, target, attrs in self.graph.edges(data=True):

            relation = attrs.get("relation", "")

            color = self.EDGE_COLORS.get(
                relation,
                "#9CA3AF",
            )

            net.add_edge(
                source,
                target,
                title=relation,
                color=color,
                arrows="to",
                width=2,
            )

        # ---------------------------------------------------
        # Save
        # ---------------------------------------------------

        net.write_html(
            output_file,
            notebook=False,
            open_browser=False,
        )

        return Path(output_file)