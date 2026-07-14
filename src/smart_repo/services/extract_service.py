from pathlib import Path
from zipfile import ZipFile


def extract_repository(zip_file: Path, extract_root: Path) -> Path:
    """
    Extract a repository ZIP file.

    Args:
        zip_file: Path to uploaded ZIP.
        extract_root: Root extraction directory.

    Returns:
        Path of extracted repository.
    """

    repository_name = zip_file.stem
    destination = extract_root / repository_name

    if destination.exists():
        import shutil
        shutil.rmtree(destination)

    destination.mkdir(parents=True, exist_ok=True)

    with ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(destination)

    return destination