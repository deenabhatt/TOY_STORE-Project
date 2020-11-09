"""Server for TOY SHOP app."""

from flask import Flask, render_template

app = Flask(__name__)


# Replace this with routes and view functions!

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/add_a_toy')
def add_a_toy():
    return render_template('add_a_toy.html')
    """show add a toy page"""

    
@app.route('/sign_up')
def sign_up_page():
    return render_template('Sign_up.html')




# @app.route("/name")
# def user(name):
#     return f"Hello{name}!"


# @app.route("/login", methods=["GET"])
# def show_login():
#     """Show login form."""

#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def process_login():
#     """Log user into site.

#     Find the user's login credentials located in the 'request.form'
#     dictionary, look up the user, and store them in the session.
#     """






if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
