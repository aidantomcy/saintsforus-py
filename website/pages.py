from flask import Blueprint, render_template

pages = Blueprint("pages", __name__, template_folder="templates")

@pages.route("/stanthony")
def stanthony():
    return render_template("stanthony.html")

