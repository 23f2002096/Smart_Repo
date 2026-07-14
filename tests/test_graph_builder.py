from pathlib import Path

from smart_repo.graph.graph_builder import GraphBuilder
from smart_repo.parser.repository_parser import RepositoryParser


repository = RepositoryParser(
    Path("src")
).parse()

builder = GraphBuilder()

graph = builder.build(repository)

print()

print("Nodes :", graph.number_of_nodes())

print("Edges :", graph.number_of_edges())