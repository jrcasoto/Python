from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def index():
    return "Index"
    
# @app.route("/hello")
# def hello():
#     return "Hello"

# @app.route("/<string:name>")
# def hello(name):
#     return render_template('template1.html', name=name)

@app.route("/<string:name>")
def hello(name):
    return render_template('template2.html', name=name)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)