from flask import Flask

from smart_repo.config import Config
from smart_repo.routes import home_bp, upload_bp, dashboard_bp, repository_bp


def create_app():
    app = Flask(
        __name__,
        template_folder=str(Config.TEMPLATE_FOLDER),
        static_folder=str(Config.STATIC_FOLDER),
    )

    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["UPLOAD_FOLDER"] = str(Config.UPLOAD_FOLDER)

    app.register_blueprint(home_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(repository_bp)

    return app