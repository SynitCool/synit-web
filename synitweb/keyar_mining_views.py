from flask import Blueprint, render_template

keyar_mining = Blueprint('keyar_mining', __name__)

@keyar_mining.route("/keyar-mining")
def base():
    return render_template("keyar_mining/index_keyar.html")

@keyar_mining.route("/keyar-mining/home")
def home():
    return render_template("keyar_mining/home_pages/home.html")

@keyar_mining.route("/keyar-mining/about")
def about():
    return render_template("keyar_mining/about_pages/about.html")