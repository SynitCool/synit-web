from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def base():
    return render_template("index.html")

@views.route('/project')
def project():
    return render_template("synit_web/project_pages/overview_project.html")

@views.route('/home')
def home():
    return render_template("synit_web/home_pages/home.html")

@views.route('/collections')
def collections():
    return render_template("synit_web/collections_pages/collections_pages.html")

@views.route('/about')
def about():
    return render_template("synit_web/about_pages/about.html")

@views.route("/api/dl_api")
def dl_api():
    return "<p class='text-center'>not available yet</p>"