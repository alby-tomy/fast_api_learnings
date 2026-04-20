from fastapi import Body, FastAPI, Path, Query, HTTPException, status
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


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)): # this is how we can define path parameters in fastAPI and also we can add validation to the path parameter using Path function
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(ge=0, le=5)): # this is how we can define query parameters in fastAPI and also we can add validation to the query parameter using Query function
    books_by_rating = [book for book in BOOKS if book.rating == rating]
    return books_by_rating


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return new_book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update-book/",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(updated_book: BookRequest):
    book_changes = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == updated_book.id:
            BOOKS[i] = update_book
            book_changes = True
    if not book_changes:
        raise HTTPException(status_code=404, detail='Item not found')
        

@app.delete("/books/delete-book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
        if not book_changed:
            raise HTTPException(status_code=404, details='Item not found')


'''
Assignment

Here is your opportunity to keep learning!
Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012).So, this book as published on the year of 2012.
Enhance each Book to now have a published_date
Then create a new GET Request method to filter by published_date
'''

@app.get("/books/published_date/",status_code=status.HTTP_200_OK)
async def read_book_by_published_date(published_date:int = Query(ge=1999, lt=2031)):
    books_by_published_date = [book for book in BOOKS if book.publish_date == published_date]
    return books_by_published_date


'''
STATUS CODE
 - An HTTP Status Code is used to help the client (the user or submitting data to the server) to understand what happened on the server side application.
 - Ther are international standards on how a Client/Server should handle the resulr of a request.
 - It allows everyone who sends a request to understand what happened on the server side application [success/failure].
 - Common Status Code
    - 1xx - Informational Responses : Request Processing
    - 2xx - Success: Request Successfully Completed
    - 3xx - Redirection : Further Action Required to Complete the Request
    - 4xx - Client Errors : An error was caused by the client
    - 5xx - Server Errors : An error occurred on the server

    HTTP Status Codes Cheat Sheet

    2xx — Success
    200 OK → Request successful (GET/PUT/DELETE with response)
    201 Created → Resource created successfully (POST)
    204 No Content → Request successful, no response body (DELETE/PUT)

    4xx — Client Errors
    400 Bad Request → Invalid request (syntax/format issue)
    401 Unauthorized → Authentication required or failed
    403 Forbidden → Authenticated but no permission
    404 Not Found → Resource does not exist
    409 Conflict → Duplicate or state conflict
    422 Unprocessable Entity → Validation failed (correct syntax, invalid data)
    429 Too Many Requests → Rate limit exceeded

    5xx — Server Errors
    500 Internal Server Error → Generic server failure
    502 Bad Gateway → Invalid response from upstream server
    503 Service Unavailable → Server overloaded or under maintenance
    504 Gateway Timeout → Upstream server timeout

'''