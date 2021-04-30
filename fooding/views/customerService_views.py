from flask import Blueprint, render_template


bp = Blueprint('customerService', __name__, url_prefix='/')

@bp.route('/customerService.html')
def customerService():
    return render_template("customerService.html")

