from pathlib import Path
from pprint import pprint

from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.repository_store import RepositoryStore
from smart_repo.services.retrieval_service import RetrievalService


repository = RepositoryParser(
    Path("src")
).parse()

RepositoryStore.save(repository)

service = RetrievalService()

results = service.retrieve(
    "scanner"
)

print("\nResults Found:", len(results))
print("-" * 60)

for item in results:
    pprint(item)