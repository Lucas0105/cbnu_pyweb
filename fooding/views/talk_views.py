from flask import Blueprint, render_template


bp = Blueprint('talk', __name__, url_prefix='/')

@bp.route('/talk.html')
def talk():
    return render_template("talk.html")

