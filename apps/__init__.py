from flask import Flask

import settings
from apps.users.view import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.register_blueprint(user_bp)

    return app