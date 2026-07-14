from pathlib import Path

from flask import current_app
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def save_repository(file: FileStorage) -> str:
    """
    Save the uploaded repository ZIP file.

    Args:
        file: Uploaded ZIP file.

    Returns:
        Saved filename.
    """

    upload_folder = Path(current_app.config["UPLOAD_FOLDER"])
    upload_folder.mkdir(parents=True, exist_ok=True)

    filename = secure_filename(file.filename)

    file.save(upload_folder / filename)

    return filename