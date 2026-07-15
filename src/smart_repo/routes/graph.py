from flask import Blueprint, abort, send_file

from smart_repo.config import Config

graph_bp = Blueprint(
    "graph",
    __name__,
)


@graph_bp.route("/graph")
def graph():

    return send_file(
        Config.GRAPH_FOLDER / "knowledge_graph.html"
    )