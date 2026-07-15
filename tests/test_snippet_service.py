from pathlib import Path

from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.snippet_service import SnippetService


repository = RepositoryParser(
    Path("src")
).parse()

for parsed_file in repository.files:

    if parsed_file.classes:

        cls = parsed_file.classes[0]

        print("=" * 80)

        print(cls.name)

        print("=" * 80)

        snippet = SnippetService.extract(
            parsed_file,
            cls.line_number,
            cls.end_line,
        )

        print(snippet)

        break