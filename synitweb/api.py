from flask import Blueprint, render_template

api = Blueprint("api", __name__)

# Route about related to api 
@api.route('/api/machine-learning')
def ml_page():
    return render_template("api_pages/mlPage_base.html")

@api.route('/api/deep-learning')
def dl_page():
    return render_template("api_pages/dlPage_base.html")