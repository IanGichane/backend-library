from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    author: str
    genre: str
    sub_genre: str
    publication_year: int
    ISBN: int
    copies_available: int
    synopsis: str
    cover_image: str
    
class userSchema(BaseModel):
    username :str
    email:str



class bookingSchema(BaseModel):
    book_id: int
    name: str
    email: str
    date: str


  
  
    