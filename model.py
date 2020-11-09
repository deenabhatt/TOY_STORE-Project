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
    # address_id = db.Column(db.Integer,db.ForeignKey('users.address_id'))
    

    toy = db.relationship('Toy', backref='users')
    user = db.relationship('User', backref='users')


    def __repr__(self):
        return f'<User user_id={self.user_id}user_fname={self.user_fname} user_lname={self.user_lname} users_email={self.user_email}>'



class Category(db.Model):
    """category."""

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String)
    category_description = db.Column(db.String)
   
    
    def __repr__(self):
        return f'<Category category_id={self.category_id} category_name={self.category_name}category_description={self.category_description} score={self.score} >'

class Toy(db.Model):

    """Toy"""

    __tablename__= 'toys'

    toy_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.category_id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    toy_name = db.Column(db.String)
    toy_description = db.Column(db.String)
    toy_manufacture = db.Column(db.String)
    toy_age = db.Column(db.Integer)

    Category = db.relationship('Category', backref='toys')
    user = db.relationship('User', backref='toys')


    def __repr__(self):
        return f'<Toy toy_id={self.toy_id} toy_name={self.toy_name} toy_description = {self.toy_description}toy_manufacture = {self.toy_manufacture} toy_age = {self.toy_age}>'

    
class Feature(db.Model):
    """feature."""

    __tablename__ = 'features'

    feature_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weight = db.Column(db.Integer)
    height= db.Column(db.Integer)
    depth = db.Column(db.Integer)
    color = db.Column(db.String)
    theame = db.Column(db.String)
    
    def __repr__(self):
        return f'<Feature feature_id={self.feature_id}weight={self.weight}height = {self.height} depth = {self.depth} color={self.color} theame = {self.theame}>'



class Toy_Feature(db.Model):
    """toy_feature."""

    __tablename__ = 'toys_Features'

    toy_feature_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    toy_id = db.Column(db.ForeignKey('toys.toy_id'))
    feature_id = db.Column(db.ForeignKey('features.feature_id'))
    store_id = db.Column(db.ForeignKey('stores.store_id'))
   
    movie = db.relationship('Toy', backref='toy_features')
    user = db.relationship('Feature', backref='toy_feature')

    def __repr__(self):
        return f'<Toy_feature Toy_id={self.toy_id} toy_feature_id={self.toy_feature_id}>'


class Store(db.Model):
    """store."""

    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    store_name = db.Column(db.String)
    store_website= db.Column(db.String)
    web_only_indicator = db.Column(db.String)
    address_id = db.Column(db.String)
    
     def __repr__(self):
         return f'<Store store_id={self.store_id} store_name={self.store_name} store_website{self.store_website} web_only_indicator{self.web_only_indicator} address_id{self.address_id},>'

class Price(db.Model):
    """price."""

    __tablename__ = 'prices'

    price_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    toy_id = db.Column(db.Integer, db.ForeignKey('toys.toy_id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    prices_dollars = db.Column(db.Integer)
    price_effective_date = db.Column(db.Integer)
    price_end_date= db.Column(db.Integer) 
    
    
    toy = db.relationship('Toy', backref='prices')
    store = db.relationship('Store', backref='prices')

    def __repr__(self):
        return f'<price price_id={self.price_id} price_dollars={self.price_dollars}price_effective_date ={self.price_effective_date}price_end_date={self.price_end_date}>'


class Address(db.Model):
    """address."""

    __tablename__ = 'addresses'

    address_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    user_id = db.Column(db.Integer,db.ForeignKey('useres.user_id')))
    address_line1 = db.Column(db.String)
    address_line2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.Integer)


    store = db.relationship('Store', backref='addresses')
    user = db.relationship('User', backref='addresses')

    def __repr__(self):
        return f'<Address address_id={self.address_id} address_line1= {self.address_line1} address_line2= {self.address_line2}city= {self.city} state=zip_code={self.zip_code}>'


def connect_to_db(flask_app, db_uri='postgresql:///toyshop', echo=True):
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

#   d = User(username="Cheese", email="eeemail", password="pppassword")
#     f = Following(subscriber=s, creator=c)


    
    