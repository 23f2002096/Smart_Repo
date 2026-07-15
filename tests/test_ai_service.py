from pathlib import Path

from smart_repo.parser.repository_parser import RepositoryParser
from smart_repo.services.ai_service import AIService
from smart_repo.services.repository_store import RepositoryStore

# Parse repository
repository = RepositoryParser(
    Path("src")
).parse()

# Store repository
RepositoryStore.save(repository)

# Ask AI
ai = AIService()

answer = ai.ask(
    "Explain RepositoryScanner."
)

print("\n" + "=" * 80)
print("AI ANSWER")
print("=" * 80)
print(answer)