"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb users')
os.system('createdb users')

os.system('dropdb categories')
os.system('createdb categories')

os.system('dropdb toys')
os.system('createdb toys')

os.system('dropdb features')
os.system('createdb features')

os.system('dropdb toys_features')
os.system('createdb toys_features')

os.system('dropdb stores')
os.system('createdb stores')

os.system('dropdb address')
os.system('createdb address')

db.create_all()

model.connect_to_db(server.app)
model.db.create_all()

Load toy_store data from JSON file
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