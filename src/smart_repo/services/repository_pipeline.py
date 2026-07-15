from pathlib import Path

from smart_repo.graph.graph_builder import GraphBuilder
from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.analytics import RepositoryAnalytics
from smart_repo.services.extract_service import extract_repository
from smart_repo.services.upload_service import save_repository
from smart_repo.config import Config
from smart_repo.services.repository_store import RepositoryStore
from smart_repo.graph.graph_visualizer import GraphVisualizer


class RepositoryPipeline:
    """
    Complete repository analysis pipeline.

    Workflow:
        Upload ZIP
            ↓
        Extract Repository
            ↓
        Parse Repository
            ↓
        Build Knowledge Graph
            ↓
        Generate Analytics
            ↓
        Return Result
    """

    def __init__(self):
        self.analytics = RepositoryAnalytics()
        self.graph_builder = GraphBuilder()
        self.graph_visualizer = GraphVisualizer

    def analyze(self, uploaded_file):
        """
        Execute the complete repository analysis pipeline.
        """

        # ------------------------------------
        # Save uploaded ZIP
        # ------------------------------------
        zip_path = save_repository(uploaded_file)

        # ------------------------------------
        # Extract ZIP
        # ------------------------------------
        repository_path = extract_repository(
            zip_path,
            Config.EXTRACT_FOLDER,
        )

        # ------------------------------------
        # Parse Repository
        # ------------------------------------
        parser = RepositoryParser(
            Path(repository_path)
        )

        repository = parser.parse()
        RepositoryStore.save(repository)

        # ------------------------------------
        # Build Knowledge Graph
        # ------------------------------------
        graph = self.graph_builder.build(repository)

        # ------------------------------------
        # Generate Interactive Graph
        # ------------------------------------

        graph_path = Config.GRAPH_FOLDER / "knowledge_graph.html"

        Config.GRAPH_FOLDER.mkdir(
            parents=True,
            exist_ok=True,
        )

        visualizer = GraphVisualizer(graph)

        visualizer.visualize(
            str(graph_path)
        )

        # ------------------------------------
        # Generate Analytics
        # ------------------------------------
        analytics = self.analytics.analyze(repository)

        # ------------------------------------
        # Return everything
        # ------------------------------------
        return {
            "repository": repository,
            "graph": graph,
            "graph_file": graph_path,
            "analytics": analytics,
        }