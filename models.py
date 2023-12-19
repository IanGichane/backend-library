from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, Integer, func, String,ForeignKey,DateTime
from sqlalchemy.orm import relationship,backref
from datetime import datetime

#create a base model
Base = declarative_base()


# define user model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(Text(), unique=True, index=True)
    email = Column(Text(), unique=True, index=True)

    bookings = relationship('Booking', back_populates='user')
# define book model
class Book(Base):
    __tablename__ = "books"

    

    #define columns
    id = Column(Integer(), primary_key=True)
    title = Column(String, index=True)
    author = Column(String)
    genre = Column(Text(), nullable=False)
    sub_genre = Column(Text(), nullable=False)
    publication_year = Column(Integer(), nullable=False)
    ISBN = Column(Integer(), nullable=False)
    copies_available = Column(Integer(), nullable=False)
    synopsis = Column(Text(), nullable=False)
    cover_image = Column(VARCHAR(), nullable=False)

    users_books = relationship('Booking', back_populates='book')

# A users borrows a book
class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    booking_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    #foreign keys
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    book = relationship("Book", back_populates="users_books")
    user = relationship("User", back_populates="bookings")


