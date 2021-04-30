from flask import Blueprint, render_template


bp = Blueprint('recipe', __name__, url_prefix='/')

@bp.route('/recipe.html')
def recipe():
    return render_template("recipe.html")

