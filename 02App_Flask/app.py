from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/") # Defaut page, the function bellow is run
# def index():
#     return "Hello, world!!"

@app.route("/")
def index():
    return render_template("index.html")