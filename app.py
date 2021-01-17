from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/rest")
def rest():
    return render_template("rest.html")


@app.route("/exercise")
def exercise():
    return render_template("exercise.html")