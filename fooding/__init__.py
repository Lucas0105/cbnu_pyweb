from flask import Flask, g, request, Response, make_response
from datetime import datetime, date

app = Flask(__name__)   # fooding 
app.debug = True

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