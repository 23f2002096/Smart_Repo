from flask import Blueprint, render_template

from smart_repo.services.repository_store import RepositoryStore

repository_bp = Blueprint(
    "repository",
    __name__,
)


@repository_bp.route("/files")
def files():

    repository = RepositoryStore.get()

    if repository is None:
        return "No repository uploaded."

    return render_template(
        "repository.html",
        repository=repository,
    )