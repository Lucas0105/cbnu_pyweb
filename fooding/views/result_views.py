from flask import Blueprint, render_template, request
from flask import session
import pymysql

bp = Blueprint('result', __name__, url_prefix='/')

@bp.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        foodname = request.form['search']
    else:
        foodname = " "

    db = pymysql.connect(host='fooding-db.ccdrxs6wuzho.us-east-2.rds.amazonaws.com', port=3306, user='admin', passwd='fooding!',
                    db='fooding_db', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT sum(like_num) FROM FoodInfo WHERE fooding_name=%s"
    

    cursor.execute(sql, foodname)
    like_num = cursor.fetchall()
    db.close()
    if 'user' in session:
        return render_template("result.html", name = session['user'], like = like_num[0][0])
    else:
        return render_template("result.html", like = like_num[0][0])

