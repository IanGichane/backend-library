from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# connect to postgress db
DATABASE_URL = "postgresql://admin:3bUURIyLFIfahbD2Rrng6WI8znNCUVw7@dpg-clua2b6d3nmc73a8pcbg-a.frankfurt-postgres.render.com/books_wgku"
engine = create_engine(DATABASE_URL, echo=True)


# connect to sessionmaker
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def method to get db
def get_db():
    db = Session()
    try:
        yield db

    finally:
        db.close()