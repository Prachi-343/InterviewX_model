from .database import init_db

def init_app(app):
    init_db(app)