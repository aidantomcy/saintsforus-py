from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv
from .views import views
from .pages import pages


load_dotenv()
secret_key = getenv("SECRET_KEY")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret_key

    app.register_blueprint(views)
    app.register_blueprint(pages)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html")

    @app.errorhandler(500)
    def server_error(e):
        return render_template("500.html")

    return app
