from flask import Blueprint, render_template
from flask import session

bp = Blueprint('rec', __name__, url_prefix='/')

@bp.route('/rec.html')
def rec():
    if 'user' in session:
        return render_template("rec.html", name = session['user'])
    else:
        return render_template("rec.html")

