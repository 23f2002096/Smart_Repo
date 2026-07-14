from dataclasses import dataclass


@dataclass
class GraphNode:
    id: str
    label: str
    node_type: str


@dataclass
class GraphEdge:
    source: str
    target: str
    relationship: str