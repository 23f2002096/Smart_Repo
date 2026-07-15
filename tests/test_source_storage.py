from pathlib import Path

from smart_repo.parser.repository_parser import RepositoryParser

repository = RepositoryParser(
    Path("src")
).parse()

for parsed_file in repository.files:

    if parsed_file.source_code.strip():

        print("=" * 80)
        print(parsed_file.file.relative_path)
        print("=" * 80)

        print(parsed_file.source_code[:800])

        break