from pathlib import Path

from smart_repo.config import Config
from smart_repo.parser.scanner import RepositoryScanner
from smart_repo.services.extract_service import extract_repository
from smart_repo.services.upload_service import save_repository


def analyze_repository(file):
    """
    Complete repository analysis pipeline.
    """

    zip_path = save_repository(file)

    extracted_path = extract_repository(
        zip_path,
        Config.EXTRACT_FOLDER,
    )

    scanner = RepositoryScanner(extracted_path)
    python_files = scanner.scan()

    return {
        "repository": extracted_path.name,
        "repository_path": extracted_path,
        "python_files": python_files,
        "total_python_files": len(python_files),
    }