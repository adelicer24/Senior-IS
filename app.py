# Import Flask library to create a Flask application
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Creates a URL route to the home page
@app.route("/")
def index():
    return render_template("base-templates/index.html")

# Creates a URL route to the about page
@app.route("/about")
def about():
    return render_template("base-templates/about.html")

# Creates a URL route to the statistics page
@app.route("/statistics")
def statistics():
    return render_template("base-templates/statistics.html")

# Creates a URL route to the statistic comparisons page
@app.route("/comparison")
def comparison():
    return render_template("base-templates/comparison.html")

# Creates a URL route to the glossary page
@app.route("/glossary")
def glossary():
    return render_template("base-templates/glossary.html")

# Creates a URL route to the player awards page
@app.route("/statistics-awards")
def awards():
    return render_template("stat-templates/awards.html")

# Creates a URL route to the standard batting statistics page for 2023
@app.route("/statistics-battingstd2023")
def battingstd2023():
    return render_template("stat-templates/2023/batting-std2023.html")

# Creates a URL route to the advanced batting statistics page for 2023
@app.route("/statistics-battingadv2023")
def battingadv2023():
    return render_template("stat-templates/2023/batting-adv2023.html")

# Creates a URL route to the sabermetric batting statistics page for 2023
@app.route("/statistics-battingsab2023")
def battingsab2023():
    return render_template("stat-templates/2023/batting-sab2023.html")

# Creates a URL route to the standard fielding statistics page for 2023
@app.route("/statistics-fieldingstd2023")
def fieldingstd2023():
    return render_template("stat-templates/2023/fielding-std2023.html")

# Creates a URL route to the advanced fielding statistics page for 2023
@app.route("/statistics-fieldingadv2023")
def fieldingadv2023():
    return render_template("stat-templates/2023/fielding-adv2023.html")

# Creates a URL route to the standard pitching statistics page for 2023
@app.route("/statistics-pitchingstd2023")
def pitchingstd2023():
    return render_template("stat-templates/2023/pitching-std2023.html")

# Creates a URL route to the advanced pitching statistics page for 2023
@app.route("/statistics-pitchingadv2023")
def pitchingadv2023():
    return render_template("stat-templates/2023/pitching-adv2023.html")

# Creates a URL route to the sabermetric pitching statistics page for 2023
@app.route("/statistics-pitchingsab2023")
def pitchingsab2023():
    return render_template("stat-templates/2023/pitching-sab2023.html")

# Creates a URL route to the standard batting statistics page for 2022
@app.route("/statistics-battingstd2022")
def battingstd2022():
    return render_template("stat-templates/2022/batting-std2022.html")

# Creates a URL route to the advanced batting statistics page for 2022
@app.route("/statistics-battingadv2022")
def battingadv2022():
    return render_template("stat-templates/2022/batting-adv2022.html")

# Creates a URL route to the sabermetric batting statistics page for 2022
@app.route("/statistics-battingsab2022")
def battingsab2022():
    return render_template("stat-templates/2022/batting-sab2022.html")

# Creates a URL route to the standard fielding statistics page for 2022
@app.route("/statistics-fieldingstd2022")
def fieldingstd2022():
    return render_template("stat-templates/2022/fielding-std2022.html")

# Creates a URL route to the advanced fielding statistics page for 2022
@app.route("/statistics-fieldingadv2022")
def fieldingadv2022():
    return render_template("stat-templates/2022/fielding-adv2022.html")

# Creates a URL route to the standard pitching statistics page for 2022
@app.route("/statistics-pitchingstd2022")
def pitchingstd2022():
    return render_template("stat-templates/2022/pitching-std2022.html")

# Creates a URL route to the advanced pitching statistics page for 2022
@app.route("/statistics-pitchingadv2022")
def pitchingadv2022():
    return render_template("stat-templates/2022/pitching-adv2022.html")

# Creates a URL route to the sabermetric pitching statistics page for 2022
@app.route("/statistics-pitchingsab2022")
def pitchingsab2022():
    return render_template("stat-templates/2022/pitching-sab2022.html")

# Creates a URL route to the standard batting statistics page for 2021
@app.route("/statistics-battingstd2021")
def battingstd2021():
    return render_template("stat-templates/2021/batting-std2021.html")

# Creates a URL route to the advanced batting statistics page for 2021
@app.route("/statistics-battingadv2021")
def battingadv2021():
    return render_template("stat-templates/2021/batting-adv2021.html")

# Creates a URL route to the sabermetric batting statistics page for 2021
@app.route("/statistics-battingsab2021")
def battingsab2021():
    return render_template("stat-templates/2021/batting-sab2021.html")

# Creates a URL route to the standard fielding statistics page for 2021
@app.route("/statistics-fieldingstd2021")
def fieldingstd2021():
    return render_template("stat-templates/2021/fielding-std2021.html")

# Creates a URL route to the advanced fielding statistics page for 2021
@app.route("/statistics-fieldingadv2021")
def fieldingadv2021():
    return render_template("stat-templates/2021/fielding-adv2021.html")

# Creates a URL route to the standard pitching statistics page for 2021
@app.route("/statistics-pitchingstd2021")
def pitchingstd2021():
    return render_template("stat-templates/2021/pitching-std2021.html")

# Creates a URL route to the advanced pitching statistics page for 2021
@app.route("/statistics-pitchingadv2021")
def pitchingadv2021():
    return render_template("stat-templates/2021/pitching-adv2021.html")

# Creates a URL route to the sabermetric pitching statistics page for 2021
@app.route("/statistics-pitchingsab2021")
def pitchingsab2021():
    return render_template("stat-templates/2021/pitching-sab2021.html")

# Creates a URL route to the standard batting statistics page for 2020
@app.route("/statistics-battingstd2020")
def battingstd2020():
    return render_template("stat-templates/2020/batting-std2020.html")

# Creates a URL route to the advanced batting statistics page for 2020
@app.route("/statistics-battingadv2020")
def battingadv2020():
    return render_template("stat-templates/2020/batting-adv2020.html")

# Creates a URL route to the sabermetric batting statistics page for 2020
@app.route("/statistics-battingsab2020")
def battingsab2020():
    return render_template("stat-templates/2020/batting-sab2020.html")

# Creates a URL route to the standard fielding statistics page for 2020
@app.route("/statistics-fieldingstd2020")
def fieldingstd2020():
    return render_template("stat-templates/2020/fielding-std2020.html")

# Creates a URL route to the advanced fielding statistics page for 2020
@app.route("/statistics-fieldingadv2020")
def fieldingadv2020():
    return render_template("stat-templates/2020/fielding-adv2020.html")

# Creates a URL route to the standard pitching statistics page for 2020
@app.route("/statistics-pitchingstd2020")
def pitchingstd2020():
    return render_template("stat-templates/2020/pitching-std2020.html")

# Creates a URL route to the advanced pitching statistics page for 2020
@app.route("/statistics-pitchingadv2020")
def pitchingadv2020():
    return render_template("stat-templates/2020/pitching-adv2020.html")

# Creates a URL route to the sabermetric pitching statistics page for 2020
@app.route("/statistics-pitchingsab2020")
def pitchingsab2020():
    return render_template("stat-templates/2020/pitching-sab2020.html")

# Creates a URL route to the standard batting statistics page for 2019
@app.route("/statistics-battingstd2019")
def battingstd2019():
    return render_template("stat-templates/2019/batting-std2019.html")

# Creates a URL route to the advanced batting statistics page for 2019
@app.route("/statistics-battingadv2019")
def battingadv2019():
    return render_template("stat-templates/2019/batting-adv2019.html")

# Creates a URL route to the sabermetric batting statistics page for 2019
@app.route("/statistics-battingsab2019")
def battingsab2019():
    return render_template("stat-templates/2019/batting-sab2019.html")

# Creates a URL route to the standard fielding statistics page for 2019
@app.route("/statistics-fieldingstd2019")
def fieldingstd2019():
    return render_template("stat-templates/2019/fielding-std2019.html")

# Creates a URL route to the advanced fielding statistics page for 2019
@app.route("/statistics-fieldingadv2019")
def fieldingadv2019():
    return render_template("stat-templates/2019/fielding-adv2019.html")

# Creates a URL route to the standard pitching statistics page for 2019
@app.route("/statistics-pitchingstd2019")
def pitchingstd2019():
    return render_template("stat-templates/2019/pitching-std2019.html")

# Creates a URL route to the advanced pitching statistics page for 2019
@app.route("/statistics-pitchingadv2019")
def pitchingadv2019():
    return render_template("stat-templates/2019/pitching-adv2019.html")

# Creates a URL route to the sabermetric pitching statistics page for 2019
@app.route("/statistics-pitchingsab2019")
def pitchingsab2019():
    return render_template("stat-templates/2019/pitching-sab2019.html")

# Creates a URL route to the standard batting statistics page for 2018
@app.route("/statistics-battingstd2018")
def battingstd2018():
    return render_template("stat-templates/2018/batting-std2018.html")

# Creates a URL route to the advanced batting statistics page for 2018
@app.route("/statistics-battingadv2018")
def battingadv2018():
    return render_template("stat-templates/2018/batting-adv2018.html")

# Creates a URL route to the sabermetric batting statistics page for 2018
@app.route("/statistics-battingsab2018")
def battingsab2018():
    return render_template("stat-templates/2018/batting-sab2018.html")

# Creates a URL route to the standard fielding statistics page for 2018
@app.route("/statistics-fieldingstd2018")
def fieldingstd2018():
    return render_template("stat-templates/2018/fielding-std2018.html")

# Creates a URL route to the advanced fielding statistics page for 2018
@app.route("/statistics-fieldingadv2018")
def fieldingadv2018():
    return render_template("stat-templates/2018/fielding-adv2018.html")

# Creates a URL route to the standard pitching statistics page for 2018
@app.route("/statistics-pitchingstd2018")
def pitchingstd2018():
    return render_template("stat-templates/2018/pitching-std2018.html")

# Creates a URL route to the advanced pitching statistics page for 2018
@app.route("/statistics-pitchingadv2018")
def pitchingadv2018():
    return render_template("stat-templates/2018/pitching-adv2018.html")

# Creates a URL route to the sabermetric pitching statistics page for 2018
@app.route("/statistics-pitchingsab2018")
def pitchingsab2018():
    return render_template("stat-templates/2018/pitching-sab2018.html")

# Creates a URL route to the team statistics page
@app.route("/statistics-teams")
def teams():
    return render_template("stat-templates/teams.html")