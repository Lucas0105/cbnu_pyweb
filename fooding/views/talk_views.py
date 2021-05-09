from flask import Blueprint, render_template
from flask import session

bp = Blueprint('talk', __name__, url_prefix='/')

@bp.route('/talk.html')
def talk():
    if 'user' in session:
        return render_template("talk.html", name = session['user'])
    else:
        return render_template("talk.html")


