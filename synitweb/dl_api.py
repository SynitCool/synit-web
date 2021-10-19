from flask import Blueprint, render_template

dl_api = Blueprint('dl_api', __name__)

@dl_api.route('/api/deep-learning')
def dl_page():
    return render_template("dlPage_base.html")