from flask import Blueprint, render_template
from flask import session

bp = Blueprint('recipe', __name__, url_prefix='/')

@bp.route('/recipe.html')
def recipe():
    if 'user' in session:
        return render_template("recipe.html", name = session['user'])
    else:
        return render_template("recipe.html")

