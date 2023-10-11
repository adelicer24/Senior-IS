from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/glossary")
def glossary():
    return render_template("glossary.html")