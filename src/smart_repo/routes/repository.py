from flask import Blueprint, abort, render_template

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


@repository_bp.route("/files/<int:file_index>")
def file_details(file_index):

    repository = RepositoryStore.get()

    if repository is None:
        return "No repository uploaded."

    if file_index >= len(repository.files):
        abort(404)

    parsed_file = repository.files[file_index]

    return render_template(
        "file_details.html",
        parsed_file=parsed_file,
    )