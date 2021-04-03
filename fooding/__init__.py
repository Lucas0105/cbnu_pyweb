from flask import Flask, g, request, Response, make_response
from flask import session, render_template, redirect, jsonify, url_for
from datetime import datetime, date, timedelta
import pymysql, bcrypt, jwt

app = Flask(__name__)   # fooding 
app.debug = True

# db = pymysql.connect(host='localhost', port=3306, user='root', passwd='753951',
#                     db='fooding_db', charset='utf8')

# app.jinja_env.trim_blocks = True # 줄 삭제

app.config.update(
    SECRET_KEY = 'X1243yRH!mMwf', #암호화 키
    SESSION_COOKIE_NAME='pyweb_flask_session',  #대표 이름
    PERMANENT_SESSION_LIFETIME=timedelta(31) #31days간 유지
)
@app.route("/home.html", methods=['GET'])
def home():
    if 'user' in session:
        return render_template("home.html", name = session['user'])
    else:
        return render_template("home.html")
        

@app.route('/register', methods=['GET','POST'])
def register():
    db = pymysql.connect(host='fooding-db.ccdrxs6wuzho.us-east-2.rds.amazonaws.com', port=3306, user='admin', passwd='fooding!',
                    db='fooding_db', charset='utf8')
    cursor = db.cursor()

    if request.method == 'POST':
        register_info = request.form
        userId = register_info['userId']
        hashed_userPassword = bcrypt.hashpw(register_info['userPassword'].encode('utf-8'), bcrypt.gensalt()) #salting 및 256해쉬 값으로 암호화
        userName = register_info['userName']
        yy = register_info['yy']
        mm = register_info['mm']
        dd = register_info['dd']
        birthday = yy + mm + dd
        gender = register_info['gender']
        email = register_info['email']
        phoneNo = register_info['phoneNo']

        if not(userId and email and hashed_userPassword and userName
                and yy and mm and dd and gender and phoneNo):
            return "입력되지 않은 정보가 있습니다"

        # print(userId, userPassword)
        sql = """
            INSERT INTO UserInfo (userid, hashed_password, username, birthdata, 
                                    gender, email, phonno)
            VALUES(%s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(sql, (userId, hashed_userPassword, userName, birthday, gender, email, phoneNo))
        db.commit()
        db.close()
        return redirect('home.html')

    else: 
        return render_template('home.html')

@app.route("/login", methods=['GET','POST'])
def login():
    db = pymysql.connect(host='fooding-db.ccdrxs6wuzho.us-east-2.rds.amazonaws.com', port=3306, user='admin', passwd='fooding!',
                    db='fooding_db', charset='utf8')
    cursor = db.cursor()

    if request.method == 'POST':
        login_info = request.form

        userId = login_info['userId']
        userPassword = login_info['userPassword']

        sql = "SELECT * FROM UserInfo WHERE userid=%s"
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
            return '', 401
            
    return render_template("home.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/rank.html')
def rank():
    if 'user' in session:
        return render_template("rank.html", name = session['user'])
    else:
        return render_template("rank.html")

@app.route('/rec.html')
def rec():
    if 'user' in session:
        return render_template("rec.html", name = session['user'])
    else:
        return render_template("rec.html")

@app.route('/customerService.html')
def customerService():
    if 'user' in session:
        return render_template("customerService.html", name = session['user'])
    else:
        return render_template("customerService.html")
# @app.route('/get_coin', methods=['POST'])
# def get_coin():
#     access_token = request.headers.get('Authorization')
#     if access_token is not None:
#         try:
#             payload = jwt.decode(access_token, 'mysecretkey', 'HS256')
#         except jwt.InvalidTokenError:
#             payload = None
        
#         if payload is None:
#             return Response(status=401)

#         user_id = payload['user_id']
#         print('payload: ', payload)

#         if int(user_id) == 4:
#             return jsonify({
#                 'bitcoin': 100
#             })
#         else:
#             return jsonify({
#                 'bitcoin': 0
#             })
#     return jsonify({
#         'bitcoin': 10
#     })


@app.route("/")  #이 request에 대한
def helloworld():
    return "Hello Flask World!" #response