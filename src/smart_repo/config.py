import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """
    Base configuration for Smart Repo.
    """

    # Project Root
    BASE_DIR = Path(__file__).resolve().parents[2]

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

    # Templates & Static
    TEMPLATE_FOLDER = BASE_DIR / "templates"
    STATIC_FOLDER = BASE_DIR / "static"

    # Data
    DATA_DIR = BASE_DIR / "data"

    UPLOAD_FOLDER = DATA_DIR / "uploads"
    EXTRACT_FOLDER = DATA_DIR / "extracted"
    GRAPH_FOLDER = DATA_DIR / "graphs"

    # SQLite
    DATABASE_PATH = DATA_DIR / "smart_repo.db"