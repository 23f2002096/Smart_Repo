from pathlib import Path

from flask import Blueprint, current_app, flash, redirect, render_template, request

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["GET", "POST"])
def upload_repository():

    if request.method == "POST":

        if "repository" not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["repository"]

        if file.filename == "":
            flash("Please choose a ZIP file.", "warning")
            return redirect(request.url)

        upload_folder = Path(current_app.config["UPLOAD_FOLDER"])
        upload_folder.mkdir(parents=True, exist_ok=True)

        file.save(upload_folder / file.filename)

        flash("Repository uploaded successfully.", "success")

        return redirect("/upload")

    return render_template("upload.html")