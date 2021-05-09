from flask import Blueprint, render_template
from flask import session

bp = Blueprint('customerService', __name__, url_prefix='/')

@bp.route('/customerService.html')
def customerService():
    if 'user' in session:
        return render_template("customerService.html", name = session['user'])
    else:
        return render_template("customerService.html")

