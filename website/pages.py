from flask import Blueprint, render_template

pages = Blueprint("pages", __name__, template_folder="templates")


@pages.route("/stanthony")
def stanthony():
    return render_template("stanthony.html")


@pages.route("/stfrancisassisi")
def stfrancisassisi():
    return render_template("stfrancisassisi.html")


@pages.route("/staidanlindisfarne")
def staidanlindisfarne():
    return render_template("staidanlindisfarne.html")


@pages.route("/stfrancisxavier")
def stfrancisxavier():
    return render_template("stfrancisxavier.html")


@pages.route("/blessedcarloacutis")
def blessedcarloacutis():
    return render_template("blessedcarloacutis.html")


@pages.route("/stagnes")
def stagnes():
    return render_template("stagnes.html")


@pages.route("/stkuriakose")
def stkuriakose():
    return render_template("stkuriakose.html")


@pages.route("/stjoan")
def stjoan():
    return render_template("stjoan.html")


@pages.route("/stpeter")
def stpeter():
    return render_template("stpeter.html")


@pages.route("/stbernadette")
def stbernadette():
    return render_template("stbernadette.html")


@pages.route("/stjohnbaptist")
def stjohnbaptist():
    return render_template("stjohnbaptist.html")
