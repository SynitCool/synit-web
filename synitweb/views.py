from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def base():
    return render_template("index.html")

@views.route('/project')
def project():
    return render_template("project_pages/overview_project.html")

@views.route('/home')
def home():
    return render_template("home_pages/home.html")

@views.route('/about')
def about():
    return render_template("about_pages/about.html")