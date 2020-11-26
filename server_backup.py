"""Server for TOY_SHOP app."""


from flask import flash, Flask, request, redirect,session, render_template
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
        session["user_email"]  = user_email
        print(session["user_email"])
        return redirect('/add_a_toy')
            
    else:
        flash("incorrect email or password")
        return redirect('/')
    

@app.route('/add_a_toy')
def add_toy():
    
    return render_template('add_a_toy.html')

@app.route('/add_a_toy', methods=["POST"])
def add_a_toy():
    print('*'*20)
    # print('\n')
    # print(request.form.get('category'))
    # print('\n')
    print('*'*20)
    category_name= request.form.get('Category')
    category = crud.create_category(category_name = category_name, category_description = "No description available")
    
    user = crud.get_user_by_email(session["user_email"])
    toy_name = request.form.get('toy_name')
    toy_description = request.form.get('toy_description')
    toy_manufacture = request.form.get('toy_manufacture')
    toy_age_range = request.form.get('toy_age_range')
    
    toy = crud.create_toy(category = category, user = user, toy_name = toy_name,toy_description = toy_description, toy_manufacture = toy_manufacture, toy_age_range = toy_age_range)
    
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
    
    return redirect('/')


@app.route('/features')
def Features():
    return render_template('features.html')


@app.route('/features', methods=["POST"])
def add_a_feature():
    print('*'*20)
    print('\n')
    print(request.form.get('theme'))
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
   

    feature = crud.create_feature(weight = weight, height = height, depth = depth, color = color, theme = theme)
    crud.create_price(toy = toy, store = store, price_dollars = price_dollars, price_effective_date = price_effective_date, price_end_date = price_end_date)
    crud.create_store(store_name = store_name, address_id = 1, store_website = store_website, web_only_indicator = web_only_indicator)
    crud.create_toy_feature(toy = toy, feature = feature)
    return redirect('/')


@app.route('/search_result')
def Search_result():

    return render_template('search_result.html')
    
@app.route('/search')
def search():
    print('*'*20)
    # print('\n')
    print(request.args.get('search'))
    # print('\n')
    search = request.args.get('search')
    toys = crud.search_toy(search)
    print (toys)
    print('*'*20)
    return render_template('search_result.html',toys = toys)


@app.route('/toy_details/<toy_id>')
def toy_details(toy_id):
    toy = crud.toy_details(toy_id)
    print(toy)
    return render_template('toy_details.html',toy = toy)






if __name__ == '__main__':
    crud.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





























































