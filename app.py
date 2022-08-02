from flask import Flask

app = Flask("Learning Flask")

@app.route("/")

def hello_world():
    return "Hello World"