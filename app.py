from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, weather!"


@app.route("/about")
def about():
    return ("Here is the information about this current page!: \n" 
    "Current status: N/A")