from flask import Blueprint, render_template


bp = Blueprint('rank', __name__, url_prefix='/')

@bp.route('/rank.html')
def rank():
    return render_template("rank.html")

