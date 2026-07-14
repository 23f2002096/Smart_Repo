from flask import (
    Blueprint,
    render_template,
    session,
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
)


@dashboard_bp.route("/dashboard")
def dashboard():

    analytics = session.get("analytics")

    if analytics is None:

        analytics = {
            "repository": "No Repository",
            "python_files": 0,
            "classes": 0,
            "functions": 0,
            "imports": 0,
            "calls": 0,
            "largest_file": "-",
            "largest_size": 0,
            "top_imports": [],
        }

    return render_template(
        "dashboard.html",
        analytics=analytics,
    )