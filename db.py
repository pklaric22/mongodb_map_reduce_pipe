from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://tbp_user:x2G3nWYf@cluster0.u8yh2mj.mongodb.net/?appName=Cluster0"


def get_movies():
    client = MongoClient(CONNECTION_STRING)
    db = client["recommender_db"]
    return list(db["movies"].find())


def get_genres():
    client = MongoClient(CONNECTION_STRING)
    db = client["recommender_db"]
    return list(db["genres"].find())
