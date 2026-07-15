from pathlib import Path

from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.summary_service import RepositorySummaryService


repository = RepositoryParser(
    Path("src")
).parse()

service = RepositorySummaryService()

summary = service.generate(repository)

print(summary)