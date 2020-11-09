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



# a = User(toy_id = null, user_fname = "aaa", user_lname = "xyz",user_email = 'aaa_xyz@test.com', address_id = null)
# b = User(toy_id = null, user_fname = "bbb", user_lname = "xyz",user_email = 'bbb_xyz@test.com', address_id = null)
# c = User(toy_id = null, user_fname = "ccc", user_lname = "pqr",user_email = 'ccc_pqr@test.com', address_id = null)


# d = Category(category_name = "Soft Toy", category_description = 'All soft toys such as teddy bears')
# e = Category(category_name = "Board games", category_description = 'All board games such as Chess')


# f = Toy(category_id = null, user_id = null, toy_name = "Teddy Bear", toy_description = Friends forever…stick together! 
#         Not only is Rainbow Friends Bear colorful as can be, but it has special paw pads so it can hold the paws of other Rainbow Friends animals.
#         If your favorite color is rainbow, then you’ll love making your own rainbow teddy bear and personalizing it with fun outfits, sounds, scents and accessories!
#         ,toy_manufacture = "buit-a-bear",toy_age = "1year to 5years")
# g = TOy(category_id = null, user_id = null, toy_name = "")

# db.session.add(a,b)
# db.session.commit()
    

# Load toy_store data from JSON file
with open('data/toy.json') as f:
    toy_data = json.loads(f.read())

# Create toy, store them in list so we can use them
# to create fake toy data


# movies_in_db = []
# for movie in movie_data:
#     title, overview, poster_path = (movie['title'],
#                                     movie['overview'],
#                                     movie['poster_path'])
#     release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

#     db_movie = crud.create_movie(title,
#                                  overview,
#                                  release_date,
#                                  poster_path)
#     movies_in_db.append(db_movie)

# # Create 10 users; each user will make 10 ratings

#     email = f'user{n}@test.com'  # Voila! A unique email!
#     password = 'test'

#     user = crud.create_user(email, password)

#     for _ in range(10):
#         random_movie = choice(movies_in_db)
#         score = randint(1, 5)

#         crud.create_rating(user, random_movie, score)