from flask import Flask, g, request, Response, make_response
from flask import session, render_template, redirect
from datetime import datetime, date, timedelta

app = Flask(__name__)   # fooding 
app.debug = True
# app.jinja_env.trim_blocks = True # 줄 삭제

app.config.update(
    SECRET_KEY = 'X1243yRH!mMwf', #암호화 키
    SESSION_COOKIE_NAME='pyweb_flask_session',  #대표 이름
    PERMANENT_SESSION_LIFETIME=timedelta(31) #31days간 유지
)


@app.route("/home.html", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        register_info = request.form
        firstName = register_info['firstName']
        lastName = register_info['lastName']
        userName = register_info['email']
        password = register_info['userPassword']
        print(userName, password, email, firstName, lastName)
        return redirect(request.url)

    return render_template('home.html')

@app.route("/rank.html")
def rank():
    return render_template("rank.html")

@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    session['Token'] = '123X'
    return make_response(res)

@app.route('/rc')
def rc():
    key = request.args.get('key') #token
    val = request.cookies.get(key)
    return "cookie['" + key +"'] = " + val + ", " + session.get('Token')

@app.route('/delsess')
def delsess():
    if session.get('Token'):
        del session['Token']
    return "Session이 삭제되었습니다!"
# @app.route('/reqenv')
# def reqenv():
#     return 'reqenv()'

def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d')) #date.today() = default 값, Year = 대문자Y
    return "우리나라 시간 형식: " + str(datestr)

# app.config['SERVER_NAME'] = 'local.com:5000'

# @app.route("/sd")
# def helloworld_local():
#     return "Hello Local.com!"

# @app.route("/sd", subdomain="g")
# def helloGworld_local():
#     return "Hello G.Local.com!!!"

@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.getlist('q')

    return "q = %s" % str(q)

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'),
                    ('Content-Length', str(len(body))) ]
        start_response('200 OK', headers)
        return [body]
    
    return make_response(application) #함수로 받으면 plain

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})  #test:ttt 헤더 편지봉투 뒷 부분
    return make_response(custom_res) #make_response -> stream으로 보냄


# @app.before_request   #어떤 request 주소를 부르기 전에 항상 실행 
# def before_request():  #euc-kr -> utf-8 Filter 역할  요즘에는 바로 써서 잘 안씀
#     print("before_request!!")
#     g.str = "한글" # 접속자 수, 방문자 수에 활용 가능 서버 이동할 때(모든 이용자 컨트롤)

 
@app.route("/gg") 
def helloworld2():
    return "Hello Flask World!"+getattr(g, 'str', '111')


@app.route("/")  #이 request에 대한
def helloworld():
    return "Hello Flask World!" #response