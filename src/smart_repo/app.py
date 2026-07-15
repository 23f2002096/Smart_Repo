from flask import Flask

from smart_repo.config import Config

from smart_repo.routes import (
    home_bp,
    upload_bp,
    dashboard_bp,
    repository_bp,
    search_bp,
    ai_bp,
)


def create_app():
    """
    Application Factory
    """

    app = Flask(
        __name__,
        template_folder=Config.TEMPLATE_FOLDER,
        static_folder=Config.STATIC_FOLDER,
    )

    # ----------------------------
    # Load Configuration
    # ----------------------------

    app.config.from_object(Config)

    # ----------------------------
    # Register Blueprints
    # ----------------------------

    app.register_blueprint(home_bp)

    app.register_blueprint(upload_bp)

    app.register_blueprint(dashboard_bp)

    app.register_blueprint(repository_bp)

    app.register_blueprint(search_bp)

    app.register_blueprint(ai_bp)
    return app