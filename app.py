from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base-templates/index.html")

@app.route("/about")
def about():
    return render_template("base-templates/about.html")

@app.route("/statistics")
def statistics():
    return render_template("base-templates/statistics.html")

@app.route("/comparison")
def comparison():
    return render_template("base-templates/comparison.html")

@app.route("/glossary")
def glossary():
    return render_template("base-templates/glossary.html")

@app.route("/statistics-awards")
def awards():
    return render_template("stat-templates/awards.html")

@app.route("/statistics-battingstd")
def battingstd():
    return render_template("stat-templates/batting-std.html")

@app.route("/statistics-battingadv")
def battingadv():
    return render_template("stat-templates/batting-adv.html")

@app.route("/statistics-battingsab")
def battingsab():
    return render_template("stat-templates/batting-sab.html")

@app.route("/statistics-fieldingstd")
def fieldingstd():
    return render_template("stat-templates/fielding-std.html")

@app.route("/statistics-fieldingadv")
def fieldingadv():
    return render_template("stat-templates/fielding-adv.html")

@app.route("/statistics-pitchingstd")
def pitchingstd():
    return render_template("stat-templates/pitching-std.html")

@app.route("/statistics-pitchingadv")
def pitchingadv():
    return render_template("stat-templates/pitching-adv.html")

@app.route("/statistics-pitchingsab")
def pitchingsab():
    return render_template("stat-templates/pitching-sab.html")

@app.route("/statistics-teams")
def teams():
    return render_template("stat-templates/teams.html")

#Next job: Fill in statistics.html with info of what stats are displayed under each category
#Then create a single batting, fielding, and pitching page