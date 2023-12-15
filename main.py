

from fastapi import FastAPI
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
@app.get('/books/{book_id}')
def get_book():
    return {}

#get all events
@app.get('/books')
def get_book_by_id(book_id):
    return []

@app.post('/books')
def create_book(book: BookSchema):
    print(book)
    return 'books created successfully'


# update
@app.patch('/books/{book_id}')
def update_book(book_id:int):
    return f'book {book_id} created successfully'


# delete
@app.delete('/books/{book_id}')
def delete_book(book_id:int):
    return f'book {book_id} deleted successfully'




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