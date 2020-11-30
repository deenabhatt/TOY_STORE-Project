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
AA = crud.create_toy(C, L,"rainbowbear","kids toy", "build a bear",3,"rainbowbear.jpg")
aa = crud.create_toy(C, N,"Gient bears","kids toy","build a bear",3,"Gient bears.jpg")
bb = crud.create_toy( A, V, "water table outdoor", "kids toy", "fisher price", 2, "water table outdoor.JPG")
cc = crud.create_toy( A, O, "scooter outdoor", "kids toy", "Razon", 3, "scooter outdoor.JPG")
dd = crud.create_toy( d, L, "pokemon", "kids toy", "Pikachu", 8, "pokemon.jpg")
ee = crud.create_toy(e, u, "monopoly", "played by two to eight players","monopoly company",8, "monopoly.jpg")
ff = crud.create_toy(B, N, "Barbie", "Indian barbie","Indian dolls comapny",8,"Barbie.jpg")
ff = crud.create_toy(B, N, "Barbie", "Indian barbie","Indian dolls comapny",8,"Barbie.jpg")
gg = crud.create_toy(B,L,"barbie 1","barbie doll","dolls comapany",5,"barbie 1.jpg")
hh = crud.create_toy(C, L,"Squishmallow", "adorable plush animals to love & cuddle","Squish Doos Pearson",1,"Squishmallow.jpg")
ii = crud.create_toy(C,O,"Llama Squishmallow","love to cuddle","squish doos Pearson",1,"Llama Squishmallow-.jpg")
jj = crud.create_toy(C,V,"Diney toys","love to cuddle disney chractors","Disney company",2,"Disney toys.gif")



z = crud.create_feature(2.5,4.0,1.8,"blue","Disney")
k = crud.create_feature(1.2,5.6,3.4,"yellow","build_a_bear")
F1 = crud.create_feature(5,10,2,"Rainbow","bear")
F2 = crud.create_feature(10,7,5,"red","barbie")
F3 = crud.create_feature(12,12,12,"pink","water table")
F4 = crud.create_feature(10,7,5,"purple","pokemon")





P = crud.create_address("1001 64th ave N","pioni","plymouth","MN",55311)
Q = crud.create_address("5001 Jewel lane", "Polaris","Maple Group","MN", 55311)
A1 = crud.create_address("101 42 nd ave S","ranch view ","minnetonka","MN",55305) 
A2 = crud.create_address("51 rosemarywoods","plan ave","Maple Grove","MN",55311)

H = crud.create_store("Target",None,"Target.com" ,"False")
J = crud.create_store("Amazon", None ,"amazon.com","True")
S1 = crud.create_store("Amazon", None ,"amazon.com","True")
S2 = crud.create_store("walmart", None ,"walmart.com","False")
S3 = crud.create_store("wayfair", None ,"wayfair.com","True")
S4 = crud.create_store("Target", None ,"Target.com","False")
S5 = crud.create_store("wayfair", None ,"wayfair.com","True")
S6 = crud.create_store("kohls", None ,"kohls.com","False")




M = crud.create_toy_feature(y,z)
N = crud.create_toy_feature(y,k)

D = crud.create_price(x, H, 15, 1112020, 11102020)
E = crud.create_price(x, J, 20, 1122020, 12122020)
p1 = crud.create_price(cc, H, 25, 11162020, 11232020)
p2 = crud.create_price(ee,S2,30,11162020,11232020)
p3 = crud.create_price(gg,S3,30,12012020,12072020)
p4 = crud.create_price(hh,S4,25,12072020,12172020)
p5 = crud.create_price(ii,S5,20,12072020,12172020)
p6 = crud.create_price(bb,S1,35,11252020,12052020)
p7 = crud.create_price(aa,S6,50,12022020,12122020)
p8 = crud.create_price(ff,S4,60,12022020,12122020)
p9 = crud.create_price(jj,S4,35,12022020,12122020)


t = crud.authenticate_user('Jiya@test.com','test')


# S = crud.create_user_toy(x,u)
# T = crud.create_user_toy(y,I)





