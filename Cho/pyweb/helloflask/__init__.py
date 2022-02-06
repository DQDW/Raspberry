from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True #G

# @app.route("/res1")
# def res1():
#     custom_res = Response("Custom Response", 200,{'test':'ttt'})
#     return make_response(custom_res)

# @app.before_request
# def before_request():
#     print("before_request!!!")
#     g.str = "한글"

# @app.route("/gg")
# def helloworld2():
#     return "Hello World" + getattr(g, 'str', '111') #111 = default

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/third")
def third():
    return render_template("third.html")
 
