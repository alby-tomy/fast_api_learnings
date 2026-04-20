from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id : int
    title : str
    author : str
    description : str
    rating : int
    publish_date : int

    def __init__(self, id, title, author, description, rating, publish_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date

class BookRequest(BaseModel):
    # beofre id : Optional[int] = None
    id : int | None = Field(default = None, description = "ID is not needed on create")
    title : str = Field(min_length=3, max_length=20)
    author : str = Field(min_length=3, max_length=20)
    description : str = Field(min_length=10, max_length=100)
    rating : int = Field(ge=0, le=5)
    publish_date : int = Field(ge=1999, lt=2031)

    model_config = {
        "json_schema_extra":{
            "example": {
                "title": "Computer Science",
                "author": "condingwithroby",
                "description": "This is a book about computer science",
                "rating": 4,
                "publish_date": 2012

            }
        }
    }


BOOKS = [
    Book(1, "Computer Science", "condingwithroby", "This is a book about computer science", 4, 2012),
    Book(2, "Python Programming", "condingwithroby", "This is a book about python programming", 5, 2013),
    Book(3, "Be Fast with FastAPI", "condingwithroby", "This is a book about FastAPI", 4, 2012),
    Book(4, "Master Endpoints", "Author 1", "This is a book about master endpoints", 5, 2015),
    Book(5, "Artificial Intelligence", "Author 2", "This is a book about artificial intelligence", 4, 2016),
    Book(6, "Data Science", "Author 3", "This is a book about data science", 5, 2012),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def read_book_by_rating(rating: int):
    books_by_rating = [book for book in BOOKS if book.rating == rating]
    return books_by_rating

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return new_book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update-book/")
async def update_book(updated_book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == updated_book.id:
            BOOKS[i] = Book(**updated_book.model_dump())
            return BOOKS[i]
        

@app.delete("/books/delete-book/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


'''
Assignment

Here is your opportunity to keep learning!
Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012).So, this book as published on the year of 2012.
Enhance each Book to now have a published_date
Then create a new GET Request method to filter by published_date
'''

@app.get("/books/published_date/{published_date}")
async def read_book_by_published_date(published_date:int):
    books_by_published_date = [book for book in BOOKS if book.publish_date == published_date]
    return books_by_published_date