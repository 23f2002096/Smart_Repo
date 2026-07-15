from smart_repo.services.repository_store import RepositoryStore
from smart_repo.services.retrieval_service import RetrievalService
from smart_repo.services.snippet_service import SnippetService
from smart_repo.services.summary_service import RepositorySummaryService


class ContextBuilder:
    """
    Builds the repository context sent to the LLM.

    Context contains:
        - Repository Summary
        - Most relevant entities
        - Source code snippets
    """

    def __init__(self):

        self.repository = RepositoryStore.get()

        self.summary_service = RepositorySummaryService()

        self.retrieval_service = RetrievalService()

    def build(self, question: str) -> str:

        if self.repository is None:
            return "No repository has been uploaded."

        context = []

        # =====================================================
        # Repository Summary
        # =====================================================

        context.append(
            self.summary_service.generate(
                self.repository
            )
        )

        context.append("")
        context.append("=" * 80)
        context.append("RELEVANT CONTEXT")
        context.append("=" * 80)

        # =====================================================
        # Retrieve Results
        # =====================================================

        results = self.retrieval_service.retrieve(question)

        if not results:

            context.append("\nNo relevant entities found.")

            return "\n".join(context)

        # =====================================================
        # Keep only the best result from each file
        # =====================================================

        best_results = {}

        for result in results:

            current = best_results.get(result["file"])

            if current is None:

                best_results[result["file"]] = result

            elif result["score"] > current["score"]:

                best_results[result["file"]] = result

        results = list(best_results.values())

        # =====================================================
        # Build Context
        # =====================================================

        for result in results:

            parsed_file = self._find_file(
                result["file"]
            )

            if parsed_file is None:
                continue

            context.append("")
            context.append("-" * 80)

            context.append(
                result["type"].upper()
            )

            context.append(
                f"File : {result['file']}"
            )

            # -------------------------------------------------
            # CLASS
            # -------------------------------------------------

            if result["type"] == "class":

                cls = next(
                    (
                        c
                        for c in parsed_file.classes
                        if c.name == result["name"]
                    ),
                    None,
                )

                if cls:

                    snippet = SnippetService.extract(
                        parsed_file,
                        cls.line_number,
                        cls.end_line,
                    )

                    context.append("")
                    context.append(f"Class : {cls.name}")
                    context.append("")
                    context.append("SOURCE CODE")
                    context.append("")
                    context.append(snippet)

            # -------------------------------------------------
            # FUNCTION
            # -------------------------------------------------

            elif result["type"] == "function":

                fn = next(
                    (
                        f
                        for f in parsed_file.functions
                        if f.name == result["name"]
                    ),
                    None,
                )

                if fn:

                    snippet = SnippetService.extract(
                        parsed_file,
                        fn.line_number,
                        fn.end_line,
                    )

                    context.append("")
                    context.append(f"Function : {fn.name}")
                    context.append("")
                    context.append("SOURCE CODE")
                    context.append("")
                    context.append(snippet)

            # -------------------------------------------------
            # FILE
            # -------------------------------------------------

            elif result["type"] == "file":

                has_entity = any(
                    (
                        r["file"] == result["file"]
                        and r["type"] in ("class", "function")
                    )
                    for r in results
                )

                if not has_entity:

                    context.append("")
                    context.append("FILE CONTENT")
                    context.append("")
                    context.append(
                        parsed_file.source_code[:1500]
                    )

            # -------------------------------------------------
            # IMPORT
            # -------------------------------------------------

            elif result["type"] == "import":

                context.append("")
                context.append(f"Import : {result['module']}")

        context.append("")
        context.append("=" * 80)

        return "\n".join(context)

    # =====================================================
    # Helper
    # =====================================================

    def _find_file(self, relative_path):

        for parsed_file in self.repository.files:

            if parsed_file.file.relative_path == relative_path:
                return parsed_file

        return None