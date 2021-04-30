from flask import Blueprint, render_template, request, session, redirect
import pymysql, bcrypt

bp = Blueprint('login', __name__, url_prefix='/')

@bp.route("/login", methods=['GET','POST'])
def login():
    db = pymysql.connect(host='fooding-db.ccdrxs6wuzho.us-east-2.rds.amazonaws.com', port=3306, user='admin', passwd='fooding!',
                    db='fooding_db', charset='utf8')
    cursor = db.cursor()

    if request.method == 'POST':
        login_info = request.form

        userId = login_info['userId']
        userPassword = login_info['userPassword']

        sql = "SELECT * FROM UserInfo1 WHERE userid=%s"
        rows_count = cursor.execute(sql, userId)
        session['name'] = userId

        if rows_count > 0:
            user_info = cursor.fetchone()
            # print("user info: ", user_info)
            pw_from_db = user_info[2]
            is_pw_correct = bcrypt.checkpw(userPassword.encode('UTF-8'), pw_from_db.encode('UTF-8'))
            
            if is_pw_correct:
                session['user'] = user_info[3]
                db.close()
                return redirect("home.html")
            else :
                db.close()
                return redirect("home.html")
                
        else:
            db.close()
            return redirect("home.html")
            
    return render_template("home.html")