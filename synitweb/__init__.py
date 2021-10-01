from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "the_secret_key_is_cool"

    from .views import views
    from .projects import projects
    from .api import api

    app.register_blueprint(views)
    app.register_blueprint(projects)
    app.register_blueprint(api)

    return app