from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv
from .views import views


load_dotenv()
secret_key = getenv('SECRET_KEY')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key

    app.register_blueprint(views)

    return app
