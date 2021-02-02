from flask import Flask, g

app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
    print("before_request!!")
    g.str = "한글" # 접속자 수, 방문자 수
 
@app.route("/gg") 
def helloworld2():
    return "Hello Flask World!"+getattr(g, 'str', '111')


@app.route("/") 
def helloworld():
    return "Hello Flask World!"