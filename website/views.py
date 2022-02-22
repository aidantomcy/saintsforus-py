from flask import Blueprint, flash, render_template, request
from dotenv import load_dotenv
from os import getenv
import smtplib
import re


load_dotenv()
views = Blueprint("views", __name__, template_folder="templates")


def check_email(email):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.fullmatch(regex, email):
        return True
    else:
        return False


@views.route("/")
@views.route("/home")
def index():
    return render_template("index.html")


@views.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
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

        is_valid_email = check_email(user_email)
        if is_valid_email:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(sender, password)
            server.sendmail(sender, receiver, body)
            server.quit()
            flash("Thank you for your feedback!")
        else:
            flash("Invalid email", category="error")

    return render_template("feedback.html")
