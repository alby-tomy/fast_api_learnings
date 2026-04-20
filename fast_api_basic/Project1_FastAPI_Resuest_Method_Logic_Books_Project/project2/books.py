from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id : int
    title : str
    author : str
    description : str
    rating : int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    # beofre id : Optional[int] = None
    id : int | None = Field(default = None, description = "ID is not needed on create")
    title : str = Field(min_length=3, max_length=20)
    author : str = Field(min_length=3, max_length=20)
    description : str = Field(min_length=10, max_length=100)
    rating : int = Field(ge=0, le=5)
    
    model_config = {
        "json_schema_extra":{
            "example": {
                "title": "Computer Science",
                "author": "condingwithroby",
                "description": "This is a book about computer science",
                "rating": 4
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science", "condingwithroby", "This is a book about computer science", 4),
    Book(2, "Python Programming", "condingwithroby", "This is a book about python programming", 5),
    Book(3, "Be Fast with FastAPI", "condingwithroby", "This is a book about FastAPI", 4),
    Book(4, "Master Endpoints", "Author 1", "This is a book about master endpoints", 5),
    Book(5, "Artificial Intelligence", "Author 2", "This is a book about artificial intelligence", 4),
    Book(6, "Data Science", "Author 3", "This is a book about data science", 5),
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