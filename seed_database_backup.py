"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb toyshop')
os.system('createdb toyshop')

# db.create_all()

model.connect_to_db(server.app)
model.db.create_all()

model.Price.query.delete()
model.Toy_Feature.query.delete()
model.Toy.query.delete()
model.User.query.delete()
model.Category.query.delete()
model.Feature.query.delete()
model.Store.query.delete()
model.Address.query.delete()


A = crud.create_category("Outdoor game", "kids toy")
B = crud.create_category("indoor toy", "kids toy")
C = crud.create_category("soft toy","everyone loves it")

u = crud.create_user("deena", "bhatt", "123@test.com","test")
I = crud.create_user("Jiya", "Dave", "Jiya@test.com","test")
L = crud.create_user("Aanya", "Pandya", "aanya@test.com","test")
N = crud.create_user("Miraya", "Pandya", "Miraya@test.com","test")
O = crud.create_user("Angiras", "Pandya", "Angira@test.com","test")
V = crud.create_user("Rohan", "Bhatt", "Rohan@test.com","test")


x = crud.create_toy( A, I, "bear", "kids toy", "disney", 5 )
y = crud.create_toy( B, u, "bear", "kids toy", "disney", 5 )

z = crud.create_feature(2.5,4.0,1.8,"blue","Disney")
k = crud.create_feature(1.2,5.6,3.4,"yellow","build_a_bear")


P = crud.create_address("1001 64th ave N","pioni","plymouth","MN",55311)
Q = crud.create_address("5001 Jewel lane", "Polaris","Maple Group","MN", 55305)


H = crud.create_store("Target",None,"Target.com" ,"False")
J = crud.create_store("Amazon", None ,"amazon.com","True")


M = crud.create_toy_feature(y,z)
N = crud.create_toy_feature(y,k)

D = crud.create_price(x, H, 5, 1112020, 11102020)
E = crud.create_price(x, J, 3, 1122020, 12122020)

t = crud.authenticate_user('Jiya@test.com','test')


# S = crud.create_user_toy(x,u)
# T = crud.create_user_toy(y,I)





