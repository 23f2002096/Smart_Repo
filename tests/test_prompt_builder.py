from pathlib import Path

from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.prompt_builder import PromptBuilder
from smart_repo.services.repository_store import RepositoryStore

repository = RepositoryParser(
    Path("src")
).parse()

RepositoryStore.save(repository)

builder = PromptBuilder()

prompt = builder.build(
    "Explain RepositoryScanner"
)

print(prompt)