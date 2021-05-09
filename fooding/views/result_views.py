from flask import Blueprint, render_template
from flask import session

bp = Blueprint('result', __name__, url_prefix='/')

@bp.route('/result.html')
def result():
    if 'user' in session:
        return render_template("result.html", name = session['user'])
    else:
        return render_template("result.html")

