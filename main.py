from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import Book,User,Booking
from schemas import BookSchema,bookingSchema




# initialize
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# define a route
@app.get('/')
def index():
    return 'welcome to my first api'


#CRUDE
# create
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



# # update
# @app.patch('/books/{book_id}')
# def update_book(book_id: int, updated_book: BookSchema, db: Session = Depends(get_db)):
#     existing_book = db.query(Book).filter(Book.id == book_id).first()
#     if existing_book is None:
#         raise HTTPException(status_code=404, detail=f'Book with id {book_id} not found')
    
    
    
#     db.commit()
#     db.refresh(existing_book)
#     return {'message': f'Book {book_id} updated successfully', 'book': existing_book}


@app.patch('/books/{book_id}')
def update_book(book_id: int):
    return {'message': f'Book {book_id} updated successfully'}


# delete
@app.delete('/books/{book_id}')
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = db.query(Book).filter(Book.id == book_id).first()
    if deleted_book is None:
        raise HTTPException(status_code=404, detail=f'Book with id {book_id} not found')
    
    db.delete(deleted_book)
    db.commit()
    return {'message': f'Book {book_id} deleted successfully'}


# # create a booking Route
# @app.post('/booking')
# def Borrow(book: BookSchema, db: Session = Depends(get_db)):

#     print(book)
#     # two stars unpacks the dictionary and  pass it as key value pairs
#     new_book = Book(**book.model_dump())
#     #Add new books to the transaction
#     db.add(new_book)
#     # commit the transaction
#     db.commit()
#     # get the book fro the db again
#     db.refresh(new_book)

#     return {'message': 'Book created successfully', 'book': new_book}

# create a booking Route
@app.post('/bookings')
def Borrow(booking: bookingSchema, db: Session = Depends(get_db)):

  
   #check if the user exists
    user = db.query(User).filter(User.email == booking.email).first()


    if user is None:
        # Does not exist so you create 
        user = User(username=booking.name, email = booking.email)
        db.add(user)
        db.commit()

        

        #After creating a user you can now create a booking
        saved_booking = Booking(booking_date = booking.date ,
                          user_id = user.id , 
                          book_id = booking.book_id)
        
        db.add(saved_booking)
        db.commit()


    else:
        # check if the user has already borrowed the book
        saved_booking = db.query(Booking).filter(Booking.user_id == user.id,
                                           Booking.book_id ==booking.book_id)


        if saved_booking == None:
            # mean the user has not yet borrowed a book
            saved_booking = db.query(Booking).filter(Booking.user_id == user.id,
                                           Booking.book_id ==booking.book_id)
            
            db.add(saved_booking)
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Book already booked")

    return {'message': 'Booking successfully'}


