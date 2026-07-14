from flask import Blueprint, flash, redirect, render_template, request

from smart_repo.services.repository_pipeline import RepositoryPipeline

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
        pipeline = RepositoryPipeline()
        result = pipeline.analyze(file)

        analytics = result["analytics"]

        flash(
            f"{analytics['repository']} analyzed successfully.",
            "success",
        )

        return render_template(
            "dashboard.html",
            analytics=result["analytics"],
        )
    return render_template("upload.html")