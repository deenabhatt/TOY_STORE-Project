"""Server for TOY SHOP app."""

from flask import Flask

app = Flask(__name__)


# Replace this with routes and view functions!

@app.route('/')
def home():
    return"Welcome! TOY SHOP<h1> Hello<h1>"

@app.route("/name")
def user(name):
    return f"Hello{name}!"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
