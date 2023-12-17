from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Text,VARCHAR,DateTime,Integer,TIMESTAMP


#create a base model
Base = declarative_base()


# define book model
class Book(Base):
    __tablename__ = 'books'

    #define columns
    id = Column(Integer(), primary_key=True)
    title =Column(Text(), nullable=False)
    author =Column(Text(),nullable=False)
    genre =Column(Text(),nullable=False)
    sub_genre =Column(Text(),nullable=False)
    publication_year=Column(Integer(),nullable=False)
    ISBN =Column(Integer(),nullable=False)
    copies_available =Column(Integer(),nullable=False)
    synopsis =Column(Text(),nullable=False)
    cover_image =Column(VARCHAR(),nullable=False)
    created__at = Column(TIMESTAMP())