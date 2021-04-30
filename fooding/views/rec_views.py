from flask import Blueprint, render_template


bp = Blueprint('rec', __name__, url_prefix='/')

@bp.route('/rec.html')
def rec():
    return render_template("rec.html")

