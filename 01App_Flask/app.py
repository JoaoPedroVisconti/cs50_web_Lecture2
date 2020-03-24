from flask import Flask

app = Flask(__name__) # Create a new aplication __name__ represent this current file

@app.route("/") # Defaut page, the function bellow is run
def index():
    return "Hello, world!!"

@app.route("/joao")
def joao():
    return "Hello Joao!!!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!!!</h1>"