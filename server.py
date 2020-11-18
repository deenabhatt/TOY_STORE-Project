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

@app.route('/', methods=["POST"])
def authenticate_user():
    print('*'*20)
    print('\n')
    print(request.form.get('email')) # request.form.get will grab from the form, matching to the name attribute in the html
    print(request.form.get('password'))
    print('\n')
    print('*'*20)
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    auth_status = crud.authenticate_user(user_email, user_password)
    if auth_status == True:
        return redirect('/add_a_toy') 
    else:
        return redirect('/')
    # return render_template('homepage.html')


@app.route('/add_a_toy')
def add_a_toy():
    return render_template('add_a_toy.html')

@app.route('/add_a_toy', methods=["POST"])
def add_a_toy():
    print('*'*20)
    print('\n')
    print(request.form.get('category'))
    print('\n')
    print('*'*20)
    category_name= request.form.get('catogory')
    user = request.form.get('user')
    toy_name = request.form.get('toy_name')
    toy_description = request.form.get('toy_description')
    toy_manufacture = request.form.get('toy_manufacture')
    toy_age_range = request.form.get('toy_age_range')
    
    
    category = crud.create_category(category_name = category_name, category_description = "No description available")
    crud.create_toy(category =category,user = user, toy_name = toy_name,toy_description = toy_description, toy_manufacture = toy_manufacture, toy_age_range = toy_age_range)
    
    return redirect('/features')

  
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




@app.route('/features')
def Features():
    return render_template('Features.html')


@app.route('/features', methods=["POST"])
def add_a_feature():
    print('*'*20)
    print('\n')
    print(request.form.get('weight'))
    print('\n')
    print('*'*20)
    weight = request.form.get('weight')
    height = request.form.get('height')
    depth = request.form.get('depth')
    color = request.form.get('color')
    theme = request.form.get('theme')

    toy = request.form.get('toy')
    store = request.form.get('store')
    price_dollars = request.form.get('price_dollars')
    price_effective_date = request.form.get('price_effective_date')
    price_end_date = request.form.get('price_end_date')

    store_name = request.form.get('store_name')
    address = request.form.get('address')
    store_website = request.form.get('store_website')
    web_only_indicator = request.form.get('web_only_indicator')
   

    crud.create_feature(weight = weight, height = height, depth = depth, color = color, theme = theme)
    crud.create_price(toy = toy, store = store, price_dollars = price_dollars, price_effective_date = price_effective_date, price_end_date = price_end_date)
    crud.create_store(store_name = store_name, address = address, store_website = store_website, web_only_indicator = web_only_indicator)
    
    # return render_template('homepage.html')
    return redirect('/feature')





if __name__ == '__main__':
    crud.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





























































