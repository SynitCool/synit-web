from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

# Route about related to netflix pages

@projects.route('/project/netflix/overview')
def netflix_overview():
    return render_template("project_pages/netflix/overview.html")

@projects.route('/project/netflix/content')
def netflix_content():
    return render_template("project_pages/netflix/content.html")

@projects.route('/project/netflix/credit')
def netflix_credit():
    return render_template("project_pages/netflix/credit.html")


# Router about related to covid-19 indonesia pages

@projects.route('/project/cvd19-ind/overview')
def cvd19Ind_overview():
    return render_template("project_pages/covid19-ind/overview.html")

@projects.route('/project/cvd19-ind/content')
def cvd19Ind_content():
    return render_template("project_pages/covid19-ind/content.html")

@projects.route('/project/cvd19-ind/credit')
def cvd19Ind_credit():
    return render_template("project_pages/covid19-ind/credit.html")

# Router about related to online shoppers pages

@projects.route('/project/online-shoppers/overview')
def onlineShoppers_overview():
    return render_template("project_pages/online-shoppers/overview.html")

@projects.route('/project/online-shoppers/content')
def onlineShoppers_content():
    return render_template("project_pages/online-shoppers/content.html")

@projects.route('/project/online-shoppers/credit')
def onlineShoppers_credit():
    return render_template("project_pages/online-shoppers/credit.html")

