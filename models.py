from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Text,VARCHAR,DateTime,Integer,TIMESTAMP


#create a base model
Base = declarative_base()


# define book model
class Book(Base):
    __tablename__ = 'books'

    #define columns
    id = Column(Integer(), primary_key=True)
    title =Column(Text())
    author =Column(Text())
    genre =Column(Text())
    sub_genre =Column(Text())
    publication_year=Column(Integer())
    ISBN =Column(Integer())
    copies_available =Column(Integer())
    synopsis =Column(Text())
    cover_image =Column(VARCHAR())
    created__at = Column(TIMESTAMP())