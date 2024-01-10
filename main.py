# https://github.com/DonatasNoreika/Python-pamokos/wiki/Flask-(įžanga)
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def user():
    return render_template("index.html")


@app.route("/5times/<text>")
def five_times(text):
    return (f"{text}\n") * 5


@app.route("/keliamieji")
def keliamieji():
    years = [x for x in range(1900, 2100) if x % 4 == 0]
    yrs_str = ""
    for x in years:
        yrs_str += f"{x} "

    return yrs_str


@app.route("/arkeliamieji", methods=["GET", "POST"])
def ar_keliamieji():
    if request.method == "POST":
        year = request.form["year"]
        if int(year) % 4 == 0:
            return f"{year} yra keliamieji"
        else:
            return f"{year} nera keliamieji"
    else:
        return render_template("check_year.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run()
