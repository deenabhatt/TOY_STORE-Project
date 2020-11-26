"""CRUD operations."""

from model import db, User, Category, Toy, Feature, Toy_Feature, Store, Price, Address, User_Toy, connect_to_db


def create_user(user_fname, user_lname, user_email, user_password):
    """Create and return a new user."""

    user = User(user_fname=user_fname,
                user_lname=user_lname,
                user_email=user_email,
                user_password=user_password
                )

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(user_email):
    
    return User.query.filter_by(user_email = user_email).first()


def authenticate_user(user_email,user_password):
    A = User.query.filter_by(user_email = user_email, user_password=user_password).first()
    print("a=", A)
    print("user_email=",user_email)
    print("user_password=",user_password)
    if A == None:
        return False
    elif A.user_password == user_password:
        return True
    else:
        return Falsefeature


def create_category(category_name, category_description):
    """Create and return a new category."""

    category = Category(category_name = category_name,
                        category_description = category_description,
                        )

    db.session.add(category)
    db.session.commit()

    return category


   
def create_toy(category,user, toy_name,toy_description, toy_manufacture, toy_age_range, toy_image):
    """Create and return a new toy."""
    print(user)
    print(category)
    toy = Toy(category_id= category.category_id,
            user_id= user.user_id,
            toy_name= toy_name,
            toy_description= toy_description,
            toy_manufacture=toy_manufacture,
            toy_age_range= toy_age_range,
            toy_image = toy_image
            )
    

    db.session.add(toy)
    print(toy)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    db.session.commit()

    return toy


def create_feature(weight,height,depth,color,theme):
    """Create and return a feature."""

    feature = Feature (weight = weight,
                    height = height,
                    depth = depth,
                    color = color,
                    theme = theme)

    db.session.add(feature)
    db.session.commit()

    return feature


def create_toy_feature(toy,feature):
    """Create and return a toy_feature."""
    print (toy)
    toy_feature = Toy_Feature(toy_id=toy.toy_id,
                            feature_id=feature.feature_id,
                            )

    db.session.add(toy_feature) 
    db.session.commit()

    return toy_feature


def create_store(store_name, address_id, store_website, web_only_indicator):
    """Create and return a store."""

    store = Store(store_name=store_name,
                address_id = address_id,
                store_website = store_website,
                web_only_indicator = web_only_indicator
                )
    

    db.session.add(store)
    db.session.commit()

    return store


def create_price(toy, store, price_dollars, price_effective_date, price_end_date):
    """Create and return a price."""

    price = Price(toy=toy,
                store=store,
                price_dollars = price_dollars,
                price_effective_date= price_effective_date,
                price_end_date = price_end_date)

    db.session.add(price)
    db.session.commit()

    return price


def create_address( address_line1, address_line2, city,state, zip_code):
    """Create and return a address."""

    address = Address(address_line1 = address_line1,
                    address_line2 = address_line2,
                    city = city,
                    state = state,
                    zip_code = zip_code
                    )

    db.session.add(address)
    db.session.commit()

    return address


def create_user_toy(toy, user):
    """Create and return a address."""

    user_toy = User_Toy(toy_id=toy, user_id=user)


    db.session.add(user_toy)
    db.session.commit()

    return user_toy

def search_toy(search):
    """Return all users."""
    toys = Toy.query.filter(Toy.toy_name.ilike("%" + search + "%")).all()
    

    return toys

def toy_details(toy_id):
    """Return all users."""
    return Toy.query.options(db.joinedload('prices')).filter(Toy.toy_id==toy_id).first()


    

def get_users():
    """Return all users."""

    return User.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    

