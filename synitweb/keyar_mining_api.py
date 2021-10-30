from flask import Blueprint, render_template

keyar_mining_api = Blueprint('keyar_mining_api', __name__)

@keyar_mining_api.route("/keyar-mining/api")
def api_overview():
    return render_template("keyar_mining/api_pages/api_overview.html")