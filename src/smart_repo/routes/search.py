from flask import Blueprint, jsonify, request

from smart_repo.services.query_service import QueryService

search_bp = Blueprint("search", __name__)


@search_bp.route("/api/search")
def search():

    query = request.args.get("q", "")

    service = QueryService()

    return jsonify(
        {
            "files": service.find_file(query),
            "functions": service.find_function(query),
            "classes": service.find_class(query),
            "imports": service.find_import(query),
        }
    )