from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
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

# get a single book by ID
@app.get('/books/{book_id}')
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail=f'Book with id {book_id} not found')
    return book
    

# get all books
@app.get('/books')
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books 

# create
@app.post('/books')
def create_book(book: BookSchema, db: Session = Depends(get_db)):

    print(book)
    # two stars unpacks the dictionary and  pass it as key value pairs
    new_book = Book(**book.model_dump())
    #Add new books to the transaction
    db.add(new_book)
    # commit the transaction
    db.commit()
    # get the book fro the db again
    db.refresh(new_book)

    return {'message': 'Book created successfully', 'book': new_book}



# update
@app.patch('/books/{book_id}')
def update_book(book_id: int, updated_book: BookSchema, db: Session = Depends(get_db)):
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if existing_book is None:
        raise HTTPException(status_code=404, detail=f'Book with id {book_id} not found')
    
    
    
    db.commit()
    db.refresh(existing_book)
    return {'message': f'Book {book_id} updated successfully', 'book': existing_book}


# delete
@app.delete('/books/{book_id}')
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = db.query(Book).filter(Book.id == book_id).first()
    if deleted_book is None:
        raise HTTPException(status_code=404, detail=f'Book with id {book_id} not found')
    
    db.delete(deleted_book)
    db.commit()
    return {'message': f'Book {book_id} deleted successfully'}


