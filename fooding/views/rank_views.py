from flask import Blueprint, render_template
from flask import session

bp = Blueprint('rank', __name__, url_prefix='/')

@bp.route('/rank.html')
def rank():
    if 'user' in session:
        return render_template("rank.html", name = session['user'])
    else:
        return render_template("rank.html")


