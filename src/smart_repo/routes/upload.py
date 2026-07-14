from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from smart_repo.services.repository_pipeline import RepositoryPipeline

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["GET", "POST"])
def upload_repository():
    """
    Upload a repository ZIP and analyze it.
    """

    if request.method == "POST":

        # ----------------------------------
        # Check uploaded file
        # ----------------------------------

        if "repository" not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["repository"]

        if file.filename == "":
            flash("Please choose a ZIP file.", "warning")
            return redirect(request.url)

        # ----------------------------------
        # Analyze Repository
        # ----------------------------------

        pipeline = RepositoryPipeline()

        result = pipeline.analyze(file)

        # ----------------------------------
        # Store data in session
        # ----------------------------------

        session["analytics"] = result["analytics"]

        flash(
            f"{result['analytics']['repository']} analyzed successfully!",
            "success",
        )

        # ----------------------------------
        # Redirect to Dashboard
        # ----------------------------------

        return redirect(
            url_for("dashboard.dashboard")
        )

    return render_template("upload.html")