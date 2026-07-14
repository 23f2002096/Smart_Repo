from pathlib import Path
import webbrowser

from smart_repo.graph.graph_builder import GraphBuilder
from smart_repo.graph.graph_visualizer import GraphVisualizer
from smart_repo.parser.repository_parser import RepositoryParser


repository = RepositoryParser(
    Path("src")
).parse()

builder = GraphBuilder()

graph = builder.build(repository)

visualizer = GraphVisualizer(graph)

output = visualizer.visualize()

print(f"\nGraph saved to: {output.resolve()}")

webbrowser.open(output.resolve().as_uri())