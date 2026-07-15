from pathlib import Path

from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.context_builder import ContextBuilder
from smart_repo.services.repository_store import RepositoryStore


# Parse repository
repository = RepositoryParser(
    Path("src")
).parse()

# Save in memory
RepositoryStore.save(repository)

# Build context
builder = ContextBuilder()

context = builder.build(
    "Explain RepositoryScanner"
)

print(context)