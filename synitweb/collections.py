from flask import Blueprint, render_template

collections = Blueprint('collections', __name__)

@collections.route("/collections")
def collections_pages():
    return render_template("collections_pages.html")