class SnippetService:
    """
    Extract source code snippets from ParsedFile.
    """

    @staticmethod
    def extract(parsed_file, start: int, end: int):

        lines = parsed_file.source_code.splitlines()

        return "\n".join(
            lines[start - 1:end]
        )