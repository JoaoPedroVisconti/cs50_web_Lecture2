from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"]) # The page accept both methods
def hello():
    if request.method == "GET":
        return "Plese submit the form instead"
    
    else: # If the method is POST
        name1 = request.form.get("name0")
        return render_template("hello.html", name0=name1)