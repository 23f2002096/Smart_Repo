from pathlib import Path
from pprint import pprint

from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.analytics import RepositoryAnalytics


repository = RepositoryParser(
    Path("src")
).parse()

analytics = RepositoryAnalytics()

result = analytics.analyze(repository)

pprint(result)