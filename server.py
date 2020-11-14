"""Server for TOY_SHOP app."""

from flask import Flask, request, redirect
from flask import render_template
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



# """Server for TOY SHOP app."""

# from flask import Flask, render_template

# app = Flask(__name__)

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/add_a_toy', methods=["GET"])
def add_a_toy():
    ''' On cick of login button, 'add a toy' page should display.
    Get email, password from homepage and pass in the Crud funtion below.'''
    # if crud.authenticate_user() = True:
    #     return render_template('add_a_toy.html')
    # else:
        # return alert ("Invalid Password")
    return "you must return a string"

  
@app.route('/sign_up')
def show_sign_up_page():

    return render_template('sign_up.html')

@app.route('/sign_up', methods=["POST"])
def sign_up_new_user():
    print('*'*20)
    print('\n')
    print(request.form.get('first_name')) # request.form.get will grab from the form, matching to the name attribute in the html
    print('\n')
    print('*'*20)
    user_fname = request.form.get('first_name')
    user_lname = request.form.get('last_name')
    user_email = request.form.get('email')
    user_password = request.form.get('psw')
    crud.create_user(user_fname =user_fname,user_lname = user_lname,user_email= user_email,user_password=user_password)
    # return render_template('homepage.html')
    return redirect('/')

@app.route('/features.html')
def Features():
    return render_template('Features.html')



@app.route("/login")
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

@app.route("/name")
def user(name):
    return f"Hello{name}!"




if __name__ == '__main__':
    crud.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





























































