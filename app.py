import flask
from flask import Flask, jsonify, request, render_template, url_for
import json

app = Flask(__name__)

# Make route website
@app.route('/')
def base():
    return render_template("index.html")

@app.route('/project')
def project():
    return render_template("project_pages/overview_project.html")

@app.route('/home')
def home():
    return render_template("home_pages/home.html")

@app.route('/about')
def about():
    return render_template("about_pages/about.html")

# Route about related to api 
@app.route('/api/machine-learning')
def ml_page():
    return render_template("api_pages/mlPage_base.html")

@app.route('/api/deep-learning')
def dl_page():
    return render_template("api_pages/dlPage_base.html")

# Route about related to netflix pages

@app.route('/project/netflix/overview')
def netflix_overview():
    return render_template("project_pages/netflix/overview.html")

@app.route('/project/netflix/content')
def netflix_content():
    return render_template("project_pages/netflix/content.html")

@app.route('/project/netflix/credit')
def netflix_credit():
    return render_template("project_pages/netflix/credit.html")


# Router about related to covid-19 indonesia pages

@app.route('/project/cvd19-ind/overview')
def cvd19Ind_overview():
    return render_template("project_pages/covid19-ind/overview.html")

@app.route('/project/cvd19-ind/content')
def cvd19Ind_content():
    return render_template("project_pages/covid19-ind/content.html")

@app.route('/project/cvd19-ind/credit')
def cvd19Ind_credit():
    return render_template("project_pages/covid19-ind/credit.html")

# Router about related to online shoppers pages

@app.route('/project/online-shoppers/overview')
def onlineShoppers_overview():
    return render_template("project_pages/online-shoppers/overview.html")

@app.route('/project/online-shoppers/content')
def onlineShoppers_content():
    return render_template("project_pages/online-shoppers/content.html")

@app.route('/project/online-shoppers/credit')
def onlineShoppers_credit():
    return render_template("project_pages/online-shoppers/credit.html")

if __name__ == '__main__':
    app.run(debug=True)