from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

# Route about related to netflix pages

@projects.route('/project/netflix/overview')
def netflix_overview():
    return render_template("synit_web/project_pages/netflix/overview.html")

@projects.route('/project/netflix/content')
def netflix_content():
    return render_template("synit_web/project_pages/netflix/content.html")

@projects.route('/project/netflix/credit')
def netflix_credit():
    return render_template("synit_web/project_pages/netflix/credit.html")


# Router about related to covid-19 indonesia pages

@projects.route('/project/cvd19-ind/overview')
def cvd19Ind_overview():
    return render_template("synit_web/project_pages/covid19-ind/overview.html")

@projects.route('/project/cvd19-ind/content')
def cvd19Ind_content():
    return render_template("synit_web/project_pages/covid19-ind/content.html")

@projects.route('/project/cvd19-ind/credit')
def cvd19Ind_credit():
    return render_template("synit_web/project_pages/covid19-ind/credit.html")

# Router about related to online shoppers pages

@projects.route('/project/online-shoppers/overview')
def onlineShoppers_overview():
    return render_template("synit_web/project_pages/online-shoppers/overview.html")

@projects.route('/project/online-shoppers/content')
def onlineShoppers_content():
    return render_template("synit_web/project_pages/online-shoppers/content.html")

@projects.route('/project/online-shoppers/credit')
def onlineShoppers_credit():
    return render_template("synit_web/project_pages/online-shoppers/credit.html")

# Route about related to mushrooms pages

@projects.route('/project/mushrooms/overview')
def mushrooms_overview():
    return render_template("synit_web/project_pages/mushrooms/overview.html")

@projects.route('/project/mushrooms/content')
def mushrooms_content():
    return render_template("synit_web/project_pages/mushrooms/content.html")

@projects.route('/project/mushrooms/credit')
def mushrooms_credit():
    return render_template("synit_web/project_pages/mushrooms/credit.html")

# Route about related to keyar-mining pages

@projects.route('/project/keyar-mining/overview')
def krmining_overview():
    return render_template("synit_web/project_pages/keyar-mining/overview.html")

@projects.route('/project/keyar-mining/content')
def krmining_content():
    return render_template("synit_web/project_pages/keyar-mining/content.html")

@projects.route('/project/keyar-mining/credit')
def krmining_credit():
    return render_template("synit_web/project_pages/keyar-mining/credit.html")