from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/home')
def home():
    return redirect(url_for('home.home'))

@bp.route('/rank')
def rank():
    return redirect(url_for('rank.rank'))

@bp.route('/rec')
def rec():
    return redirect(url_for('rec.rec'))

@bp.route('/talk')
def talk():
    return redirect(url_for('talk.talk'))

@bp.route('/recipe')
def recipe():
    return redirect(url_for('recipe.recipe'))

@bp.route('/customerService')
def customerService():
    return redirect(url_for('customerService.customerService'))

@bp.route('/rogin')
def rogin():
    return redirect(url_for('rogin.rogin'))

@bp.route('/result')
def result():
    return redirect(url_for('result.result'))
