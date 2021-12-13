from flask import Flask,render_template


app = Flask(__name__)


@app.route("/",methods = ['GET','POST'])
def starts():
    return render_template('index.html')

@app.route("/<string:name>/")
def start(name):
    return render_template("name.html",name = name)

