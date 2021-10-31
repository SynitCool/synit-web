from flask import Blueprint, render_template

keyar_mining_api = Blueprint('keyar_mining_api', __name__)

# Overview
@keyar_mining_api.route("/keyar-mining/api")
def api_overview():
    return render_template("keyar_mining/api_pages/api_overview.html")

# Association rules
@keyar_mining_api.route("/keyar-mining/api/association-rules/apriori")
def apriori():
    return render_template("keyar_mining/api_pages/association_rules/apriori.html")

@keyar_mining_api.route("/keyar-mining/api/association-rules/fpgrowth")
def fpgrowth():
    return render_template("keyar_mining/api_pages/association_rules/fpgrowth.html")

@keyar_mining_api.route("/keyar-mining/api/association-rules/evaluate")
def evaluate():
    return render_template("keyar_mining/api_pages/association_rules/evaluate.html")

# Clustering
@keyar_mining_api.route("/keyar-mining/api/clustering/kmeans")
def kmeans():
    return render_template("keyar_mining/api_pages/clustering/kmeans.html")

# Classification
@keyar_mining_api.route("/keyar-mining/api/classification/knn")
def knn():
    return render_template("keyar_mining/api_pages/classification/knn.html")
