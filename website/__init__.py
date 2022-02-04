from flask import Flask
from dotenv import load_dotenv
from os import getenv
from .views import views
from .pages import pages


load_dotenv()
secret_key = getenv('SECRET_KEY')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key

    app.register_blueprint(views)
    app.register_blueprint(pages)

    return app
