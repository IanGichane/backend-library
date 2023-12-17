

from fastapi import FastAPI,Depends
from sqlalchemy.orm import session
from database import get_db
from models import Book
from schemas import BookSchema


# initialize
app = FastAPI()


# define a route
@app.get('/')
def index():
    return 'welcome to my first api'


#CRUDE
# create

# read
# get a single event
# get a single book by ID
@app.get('/books/{book_id}')
def get_book(book_id: int):
    return {"book_id": book_id}

#get all events
@app.get('/books')
def get_all_books():
    return []

# create
@app.post('/books')
def create_book(book: BookSchema):
    print(book)
    return 'Book created successfully'



# update
@app.patch('/books/{book_id}')
def update_book(book_id: int):
    return f'Book {book_id} updated successfully'


# delete
@app.delete('/books/{book_id}')
def delete_book(book_id: int):
    return f'Book {book_id} deleted successfully'




# {
#   'title':'str'
#     'author':'str'
#     'genre':'str'
#     'sub_genre':'str'
#     'publication_year':2
#     'ISBN':int
#     'copies_available':1
#     'synopsis':'str'
#     'cover_image':'str'
# }