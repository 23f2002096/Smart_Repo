from flask import Blueprint, jsonify, render_template, request

from smart_repo.services.ai_service import AIService

ai_bp = Blueprint(
    "ai",
    __name__,
)


@ai_bp.route("/chat")
def chat():

    return render_template(
        "chat.html"
    )


@ai_bp.route("/api/chat", methods=["POST"])
def ask_ai():

    data = request.get_json()

    question = data.get(
        "question",
        "",
    ).strip()

    if not question:

        return jsonify(
            {
                "error": "Question cannot be empty."
            }
        ), 400

    ai = AIService()

    answer = ai.ask(question)

    return jsonify(
        {
            "question": question,
            "answer": answer,
        }
    )