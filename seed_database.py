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
d = crud.create_category("All other", "everyone's favorite") 
e = crud.create_category("board Game","All age group")

u = crud.create_user("deena", "bhatt", "123@test.com","test")
I = crud.create_user("Jiya", "Dave", "Jiya@test.com","test")
L = crud.create_user("Aanya", "Pandya", "aanya@test.com","test")
N = crud.create_user("Miraya", "Pandya", "Miraya@test.com","test")
O = crud.create_user("Angiras", "Pandya", "Angira@test.com","test")
V = crud.create_user("Rohan", "Bhatt", "Rohan@test.com","test")


x = crud.create_toy( C, I, "rainbowbear", "kids toy", "build a bear", 5, "rainbowbear.jpg")
y = crud.create_toy( C, u, "Gient bears", "kids toy", "build a bear", 5,"Gient bears.jpg")
AA = crud.create_toy(C, L,"rainbowbear","kids toy", "build a bear",3,"Llama Squishmallow-.jpg")
aa = crud.create_toy(C, N,"Gient bears","kids toy","build a bear",3,"barbie 1.jpg")
bb = crud.create_toy( A, V, "water table outdoor", "kids toy", "fisher price", 2, "Barbie.jpg")
cc = crud.create_toy( A, O, "scooter outdoor", "kids toy", "Razon", 3, "Disney toy world.gif")
dd = crud.create_toy( d, L, "pokemon", "kids toy", "Pikachu", 8, "pokemon.jpg")
ee = crud.create_toy(e, u, "monopoly", "played by two to eight players","monopoly company",8, "monopoly.jpg")
ff = crud.create_toy(B, N, "Barbie", "barbie doll","dolls comapany",8,"Barbie.jpg")
gg = crud.create_toy(B,L,"barbie 1","Indian barbie","Indian dolls comapny",5,"barbie 1.jpg")






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





