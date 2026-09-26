# seed_db.py
# ამ ფაილს უშვებთ მხოლოდ ერთხელ, რომ ფილმების სია ბაზაში შეიტანოთ.

from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

movies = [
    {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Sci-Fi", "duration": 148},
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Action", "duration": 136},
    {"title": "Interstellar", "year": 2014, "rating": 8.6, "genre": "Sci-Fi", "duration": 169},
    {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime", "duration": 175},
    {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime", "duration": 154},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action", "duration": 152},
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Sci-Fi", "duration": 136},
    {"title": "Interstellar", "year": 2014, "rating": 8.6, "genre": "Sci-Fi", "duration": 169},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action", "duration": 152},
    {"title": "Fight Club", "year": 1999, "rating": 8.8, "genre": "Drama", "duration": 139},
    {"title": "Forrest Gump", "year": 1994, "rating": 8.8, "genre": "Drama", "duration": 142},
    {"title": "Gladiator", "year": 2000, "rating": 8.5, "genre": "Action", "duration": 155},
    {"title": "The Shawshank Redemption", "year": 1994, "rating": 9.3, "genre": "Drama", "duration": 142},
    {"title": "The Prestige", "year": 2006, "rating": 8.5, "genre": "Drama", "duration": 130},
    {"title": "Avatar", "year": 2009, "rating": 7.8, "genre": "Sci-Fi", "duration": 162},
    {"title": "Whiplash", "year": 2014, "rating": 8.5, "genre": "Drama", "duration": 106},
    {"title": "Joker", "year": 2019, "rating": 8.4, "genre": "Drama", "duration": 122},
    {"title": "Parasite", "year": 2019, "rating": 8.5, "genre": "Thriller", "duration": 132},
    {"title": "The Wolf of Wall Street", "year": 2013, "rating": 8.2, "genre": "Biography", "duration": 180},
    {"title": "Mad Max: Fury Road", "year": 2015, "rating": 8.1, "genre": "Action", "duration": 120},
    {"title": "Django Unchained", "year": 2012, "rating": 8.4, "genre": "Western", "duration": 165},
]

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# თუ ადრე უკვე გაქვთ მონაცემები, წავშალოთ და თავიდან შევიყვანოთ
collection.delete_many({})
collection.insert_many(movies)

print(f"{len(movies)} ფილმი წარმატებით დაემატა '{DB_NAME}.{COLLECTION_NAME}' კოლექციაში.")
