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
    return render_template("project.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)