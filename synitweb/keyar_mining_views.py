from flask import Blueprint, render_template

keyar_mining = Blueprint('keyar_mining', __name__)

@keyar_mining.route("/keyar-mining")
def base():
    return render_template("index_keyar.html")