"""CRUD operations."""

from model import db, User, Category, Toy, Feature, Toy_Feature, Store, Price, Address, connect_to_db


def create_user(fname, lname,email):
    """Create and return a new user."""

    user = User(fname=user_fname,
                lname=user_lname,
                email=user_email,
                )

    db.session.add(user)
    db.session.commit()

    return user


def create_category(name, description):
    """Create and return a new category."""

    category = Category(name = category_name,
                        description = category_description,
                        )

    db.session.add(category)
    db.session.commit()

    return category


def create_toy(name,description, manufacture,age):
    """Create and return a new toy."""

    toy = Toy(name=toy_name,
            description= toy_description,
            manufacture=toy_manufacture,
            age= toy_age
            )

    db.session.add(toy)
    db.session.commit()

    return toy


def create_feature(weight,height,depth,color,theme):
    """Create and return a feature."""

   feature = Feature(weight=weight,
             height=height,
             depth = depth,
             color=color,
             theme= theame)
                                     
    db.session.add(Feature)
    db.session.commit()

    return Feature


def create_toy_feature():
    """Create and return a toy_feature."""

    toy_feature = Toy_Feature()

    db.session.add(Toy_Feature) 
    db.session.commit()

    return Toy_Feature


def create_store(name, website,web_only_indicator,address):
    """Create and return a store."""

    store = Store(name=name,
                  website = store_website,
                  web_only_indicator = store_web_only_indicator,
                  address = store_address
                  )

    db.session.add(Store)
    db.session.commit()

    return Store


def create_price(dollars, effective_date, end_date):
    """Create and return a price."""

    price = Price(dollars = price_dollars,
                   effective_date= price_effective_date,
                   end_date = price_effective_date))

    db.session.add(price)
    db.session.commit()

    return Price


    def create_address(line1, line2, city,state, zip_code):
    """Create and return a address."""

    address = Address(line1 = address_line1,
                       line2 = address_line2,
                       city = city,
                       state = state,
                       zip_code = zip_code
                       )

    db.session.add(Address)
    db.session.commit()

    return address


# def get_users():
#     """Return all users."""

#     return User.query.all()


# def get_user_by_id(user_id):
#     """Return a user by primary key."""

#     return User.query.get(user_id)


# def create_movie(title, overview, release_date, poster_path):
#     """Create and return a new movie."""

#     movie = Movie(title=title,
#                   overview=overview,
#                   release_date=release_date,
#                   poster_path=poster_path)

#     db.session.add(movie)
#     db.session.commit()

#     return movie


# def get_movies():
#     """Return all movies."""

#     return Movie.query.all()


# def get_movie_by_id(movie_id):
#     """Return a movie by primary key."""

#     return Movie.query.get(movie_id)


# def create_rating(user, movie, score):
#     """Create and return a new rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     db.session.add(rating)
#     db.session.commit()

#     return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
