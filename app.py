from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Uh, I mean Conclusion Zuyd :D"
