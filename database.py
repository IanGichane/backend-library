from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# connect to postgress db
engine = create_engine("postgresql://admin:3bUURIyLFIfahbD2Rrng6WI8znNCUVw7@dpg-clua2b6d3nmc73a8pcbg-a.frankfurt-postgres.render.com/books_wgku" ,echo=True)

# connect to sessionmaker
session = sessionmaker(bind = engine)

# def method to get db
def get_db():
    db = session()
    try:
        yield db

    finally:
        db.close()