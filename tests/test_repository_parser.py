from pathlib import Path

from smart_repo.parser.repository_parser import RepositoryParser


repository = RepositoryParser(
    Path("src")
)

parsed = repository.parse()

print()

print("Repository :", parsed.name)

print("Files      :", len(parsed.files))

print()

for file in parsed.files:

    print(file.file.relative_path)