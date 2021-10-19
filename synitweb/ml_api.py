from flask import Blueprint, render_template

ml_api = Blueprint('ml_api', __name__)

@ml_api.route('/api/machine-learning')
def ml_page():
    return render_template("synit_web/api_pages/machine_learning/ml_overview.html")

@ml_api.route('/api/machine-learning/online_shopper')
def online_shopper_page():
    return render_template("synit_web/api_pages/machine_learning/online_shopper/online_shopper_overview.html")