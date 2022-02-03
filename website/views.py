from flask import Blueprint, render_template, request, redirect, url_for
from dotenv import load_dotenv
from os import getenv
import smtplib


load_dotenv()
views = Blueprint("views", __name__, template_folder="templates")


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/feedback", methods=["GET", "POST"])
def feedback():
    name = request.form.get("name")
    user_email = request.form.get("email")
    message = request.form.get("message")

    sender = "info.saintsforus@gmail.com"
    receiver = "aidantomcy@gmail.com"
    password = getenv("EMAIL_PASSWORD")
    subject = "New form submission in Saints for Us website"
    body = f"""
There is a new form submission in the website, here are the details:

Name: {name}
Email: {user_email}
Message: {message}
"""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, password)
    server.sendmail(sender, receiver, body)

    return render_template("feedback.html")
