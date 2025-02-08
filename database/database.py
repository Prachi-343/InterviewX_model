from pymongo import MongoClient

db = None

def init_db(app):
    global db
    client = MongoClient(app.config['MONGO_URI'])
    db = client[app.config['MONGO_DBNAME']]