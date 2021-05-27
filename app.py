from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Uhm, ik bedoel Dag, Wereld :D"
