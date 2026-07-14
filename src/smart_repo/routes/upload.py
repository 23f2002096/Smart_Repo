from flask import Blueprint, flash, redirect, render_template, request

from smart_repo.services.analyzer import analyze_repository

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

        result = analyze_repository(file)

        flash(
            f"{result['repository']} uploaded successfully. "
            f"Found {result['total_python_files']} Python files.",
            "success",
        )

        return render_template(
            "upload.html",
            result=result,
        )

    return render_template("upload.html")