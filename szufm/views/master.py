from flask import Blueprint, render_template


master_app = Blueprint('home', __name__, template_folder='../templates')


@master_app.route('/')
def index():
    return render_template('index.html')
