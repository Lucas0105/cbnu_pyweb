from flask import Blueprint, render_template
from flask import session

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/home.html')
def home():
    if 'user' in session:
        return render_template("home.html", name = session['user'])
    else:
        return render_template("home.html")

