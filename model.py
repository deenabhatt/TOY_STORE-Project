"""Models for TOY_SHOP app."""

import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """users."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    toy_id = db.Column(db.Integer, db.ForeignKey('toys.toys_id'))
    user_fname = db.Column(db.String)
    user_lname = db.Column(db.String)
    user_email = db.Column(db.String, unique=True)
    address_id = db.Column(db.Integer,db.ForeignKey('users.address_id'))
    

    def __repr__(self):
        return f'<user user_id={self.user_id} users={self.user_email}>'



class Category(db.Model):
    """category."""

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String)
    category_description = db.Column(db.String)
    score = db.Column(db.Integer)
    


class Toy(db.Model):

    """Toy"""

    __tablename__= 'toys'

    Toy_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.category_id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    Toy_name = db.Column(db.String)
    toy_description = db.Column(db.String)
    toy_manufacture = db.Column(db.String)
    toy_age = db.Column(db.Integer)

    # ratings = a list of Rating objects

    # def __repr__(self):
    #     return f'<Toy Toy_id={self.Toy_id} title={self.toy}>'


class Feature(db.Model):
    """feature."""

    __tablename__ = 'features'

    feature_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weight = db.Column(db.Integer)
    height= db.Column(db.Integer)
    depth = db.Column(db.Integer)
    color = db.Column(db.String)
    theame = db.Column(db.String)
    
    # def __repr__(self):
    #     return f'<Toy Toy_id={self.Toy_id} title={self.toy}>'



class Toy_Feature(db.Model):
    """toy_feature."""

    __tablename__ = 'toys_Features'

    price_feature_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Toy_id = db.Column(db.ForeignKey('toys.toy_id'))
    feature_id = db.Column(db.ForeignKey('features.feature_id'))
    store_id = db.Column(db.ForeignKey('stores.store_id'))
   
    
    # def __repr__(self):
    #     return f'<Toy Toy_id={self.Toy_id} title={self.toy}>'


class Store(db.Model):
    """store."""

    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    store_name = db.Column(db.String)
    store_website= db.Column(db.String)
    web_only_indicator = db.Column(db.String)
    address_id = db.Column(db.String)
    
     # def __repr__(self):
     #     return f'<Toy Toy_id={self.Toy_id} title={self.toy}>'

class Price(db.Model):
    """price."""

    __tablename__ = 'prices'

    price_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    toy_id = db.Column(db.Integer, db.ForeignKey('toys.toy_id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    prices_dollars = db.Column(db.Integer)
    price_effective_date = db.Column(db.Integer)
    price_end_date= db.Column(db.Integer) 
    
    

    # def __repr__(self):
    #     return f'<user user_id={self.user_id} users={self.user_email}>'

class Address(db.Model):
    """address."""

    __tablename__ = 'addresses'

    address_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    address_line1 = db.Column(db.String)
    address_line2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.Integer)


    # movie = db.relationship('Movie', backref='ratings')
    # user = db.relationship('User', backref='ratings')

#     def __repr__(self):
#         return f'<Rating rating_id={self.rating_id} score={self.score}>'


def connect_to_db(flask_app, db_uri='postgresql:///users', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

#     # Call connect_to_db(app, echo=False) if your program output gets
#     # too annoying; this will tell SQLAlchemy not to print out every
#     # query it executes.

    connect_to_db(app)






# if name == 'main':
from server import app
connect_to_db(app)

# os.system('dropdb users')
# os.system('createdb users')

# os.system('dropdb categories')
# os.system('createdb categories')


#     os.system('dropdb toysdb')
#     os.system('createdb toysdb')


#     os.system('dropdb toysdb')
#     os.system('createdb toysdb')


#     os.system('dropdb featuresdb')
#     os.system('createdb featuresdb')


#     os.system('dropdb toys_featuresdb')
#     os.system('createdb toys_featuresdb')

#     os.system('dropdb storesdb')
#     os.system('createdb storesdb')


#     db.create_all()
a = Category(category_name = "Soft Toy", category_description = 'All soft toys such as teddy bears')
b = Category(category_name = "Board games", category_description = 'All board games such as Chess')
# c = Toys(category_id = 1, )
#   d = User(username="Cheese", email="eeemail", password="pppassword")
#     f = Following(subscriber=s, creator=c)

db.session.add(a,b)
db.session.commit()
    
    
    