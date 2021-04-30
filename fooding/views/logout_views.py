from flask import Blueprint, render_template, request
from flask import session, redirect, url_for
import pymysql, bcrypt


bp = Blueprint('logout', __name__, url_prefix='/')

@bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home.home'))