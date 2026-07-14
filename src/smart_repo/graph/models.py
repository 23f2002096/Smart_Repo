from dataclasses import dataclass, field


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


@dataclass
class GraphData:
    nodes: list[GraphNode] = field(default_factory=list)
    edges: list[GraphEdge] = field(default_factory=list)