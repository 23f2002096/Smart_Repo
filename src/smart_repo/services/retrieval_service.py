from rapidfuzz import fuzz

from smart_repo.services.repository_store import RepositoryStore

STANDARD_LIBRARIES = {
    "abc",
    "argparse",
    "ast",
    "collections",
    "contextlib",
    "copy",
    "csv",
    "dataclasses",
    "datetime",
    "functools",
    "glob",
    "hashlib",
    "heapq",
    "inspect",
    "io",
    "itertools",
    "json",
    "logging",
    "math",
    "os",
    "pathlib",
    "pickle",
    "queue",
    "random",
    "re",
    "shutil",
    "sqlite3",
    "statistics",
    "string",
    "subprocess",
    "sys",
    "tempfile",
    "threading",
    "time",
    "typing",
    "uuid",
    "zipfile",
}

class RetrievalService:
    """
    Retrieve the most relevant repository entities
    based on a user query.

    Entity Types:
        - File
        - Class
        - Function
        - Import
    """

    def __init__(self):
        self.repository = RepositoryStore.get()

    # ---------------------------------------------------------
    # Scoring Function
    # ---------------------------------------------------------

    def calculate_score(self, query: str, text: str) -> float:
        """
        Calculate similarity score.

        Priority:

        100 -> Exact Match
         95 -> Starts With
         90 -> Contains
         else -> Fuzzy Score
        """

        query = query.lower().strip()
        text = text.lower().strip()

        if query == text:
            return 100

        if text.startswith(query):
            return 95

        if query in text:
            return 90

        return max(
            fuzz.ratio(query, text),
            fuzz.partial_ratio(query, text),
            fuzz.token_sort_ratio(query, text),
        )

    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------

    def retrieve(
        self,
        query: str,
        threshold: int = 80,
        top_k: int = 20,
    ):

        if self.repository is None:
            return []

        results = []
        seen = set()

        for parsed_file in self.repository.files:

            # =====================================================
            # FILE
            # =====================================================

            score = self.calculate_score(
                query,
                parsed_file.file.name,
            )

            if score >= threshold:

                key = (
                    "file",
                    parsed_file.file.relative_path,
                )

                if key not in seen:

                    seen.add(key)

                    results.append(
                        {
                            "type": "file",
                            "score": score,
                            "file": parsed_file.file.relative_path,
                        }
                    )

            # =====================================================
            # CLASS
            # =====================================================

            for cls in parsed_file.classes:

                score = self.calculate_score(
                    query,
                    cls.name,
                )

                if score >= threshold:

                    key = (
                        "class",
                        parsed_file.file.relative_path,
                        cls.name,
                    )

                    if key not in seen:

                        seen.add(key)

                        results.append(
                            {
                                "type": "class",
                                "score": score,
                                "name": cls.name,
                                "line": cls.line_number,
                                "file": parsed_file.file.relative_path,
                            }
                        )

            # =====================================================
            # FUNCTION
            # =====================================================

            for function in parsed_file.functions:

                score = self.calculate_score(
                    query,
                    function.name,
                )

                if score >= threshold:

                    key = (
                        "function",
                        parsed_file.file.relative_path,
                        function.name,
                    )

                    if key not in seen:

                        seen.add(key)

                        results.append(
                            {
                                "type": "function",
                                "score": score,
                                "name": function.name,
                                "line": function.line_number,
                                "arguments": function.arguments,
                                "file": parsed_file.file.relative_path,
                            }
                        )

            # =====================================================
            # IMPORT
            # =====================================================

            for imp in parsed_file.imports:

                root_module = imp.module.split(".")[0]

                if root_module in STANDARD_LIBRARIES:
                    continue

                score = self.calculate_score(
                    query,
                    imp.module,
                )

                if score >= threshold:

                    key = (
                        "import",
                        parsed_file.file.relative_path,
                        imp.module,
                    )

                    if key not in seen:

                        seen.add(key)

                        results.append(
                            {
                                "type": "import",
                                "score": score,
                                "module": imp.module,
                                "file": parsed_file.file.relative_path,
                            }
                        )

        # ---------------------------------------------------------
        # Sort by score
        # ---------------------------------------------------------

        results.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return results[:top_k]