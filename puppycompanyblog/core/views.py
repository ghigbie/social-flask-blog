from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
@core.route('/index')
def index():
    return render_template('index.html')

@core.route('/info')
def info():
    return render_template('infor.html')