from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Niet slapen jongens heh :D"
