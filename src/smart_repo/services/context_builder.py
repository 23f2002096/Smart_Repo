from smart_repo.services.query_service import QueryService
from smart_repo.services.summary_service import RepositorySummaryService
from smart_repo.services.repository_store import RepositoryStore


class ContextBuilder:
    """
    Build LLM context from the parsed repository.
    """

    def __init__(self):

        self.query = QueryService()
        self.summary = RepositorySummaryService()

    def build(self, user_question: str):

        repository = RepositoryStore.get()

        if repository is None:
            return "No repository has been uploaded."

        context = []

        # --------------------------------------------------
        # Repository Summary
        # --------------------------------------------------

        context.append(
            self.summary.generate(repository)
        )

        question = user_question.lower()

        # --------------------------------------------------
        # Search Functions
        # --------------------------------------------------

        for parsed_file in repository.files:

            for function in parsed_file.functions:

                if function.name.lower() in question:

                    context.append(
                        f"\nFunction: {function.name}"
                    )

                    context.append(
                        f"File: {parsed_file.file.relative_path}"
                    )

        # --------------------------------------------------
        # Search Classes
        # --------------------------------------------------

        for parsed_file in repository.files:

            for cls in parsed_file.classes:

                if cls.name.lower() in question:

                    context.append(
                        f"\nClass: {cls.name}"
                    )

                    context.append(
                        f"File: {parsed_file.file.relative_path}"
                    )

        # --------------------------------------------------
        # Search Imports
        # --------------------------------------------------

        for parsed_file in repository.files:

            for imp in parsed_file.imports:

                if imp.module.lower() in question:

                    context.append(
                        f"\nImport: {imp.module}"
                    )

                    context.append(
                        f"File: {parsed_file.file.relative_path}"
                    )

        return "\n".join(context)