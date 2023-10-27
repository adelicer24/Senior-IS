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

@app.route("/statistics-teams")
def teams():
    return render_template("stat-templates/teams.html")

@app.route("/statistics-awards")
def awards():
    return render_template("stat-templates/awards.html")