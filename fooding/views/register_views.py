from flask import Blueprint, render_template, request
from flask import redirect
import pymysql, bcrypt


bp = Blueprint('register', __name__, url_prefix='/')

@bp.route('/register', methods=['GET','POST'])
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
            INSERT INTO UserInfo1 (userid, hashed_password, username, birthdata, 
                                    gender, email, phonno)
            VALUES(%s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(sql, (userId, hashed_userPassword, userName, birthday, gender, email, phoneNo))
        db.commit()
        db.close()
        return render_template('home.html')

    else: 
        return render_template('home.html')