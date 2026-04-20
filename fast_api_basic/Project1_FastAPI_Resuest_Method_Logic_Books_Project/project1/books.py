from fastapi import Body,FastAPI


app = FastAPI() # this allow uvicorn to identify that we are creating a new application of fastAPI and this will import all of the resources

BOOKS = [
    {"title": "Title One", "author": "Author One", 'catagory': 'science'},
    {"title": "Title Two", "author": "Author Two", 'catagory': 'science'},
    {"title": "Title Three", "author": "Author Three", 'catagory': 'history'},
    {"title": "Title Four", "author": "Author Four", 'catagory': 'math'},
    {"title": "Title Five", "author": "Author Five", 'catagory': 'math'},
    {"title": "Title Six", "author": "Author Six", 'catagory': 'math'},
]

# GET METHOD
@app.get("/books") # this is the decorator which will allow us to define the type of request method and the path of the api
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}") # this is the decorator which will allow us to define the type of request method and the path of the api with a dynamic parameter
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}

@app.get("/books/catagory/{book_catagory}") # this is the decorator which will allow us to define the type of request method and the path of the api with a dynamic parameter
async def read_book_by_catagory(book_catagory:str):
    book_list = []
    for book in BOOKS:
        if book.get("catagory").casefold() == book_catagory.casefold():
            book_list.append(book)
    return book_list

@app.get("/books/author/{book_author}") # this is the decorator which will allow us to define the type of request method and the path of the api with a dynamic parameter
async def read_book_by_author(book_author:str):
    book_list = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            book_list.append(book)
    return book_list

@app.get("/books/search/") # this is the decorator which will allow us to define the type of request method and the path of the api with a query parameter
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get("catagory").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/") # this is the decorator which will allow us to define the type of request method and the path of the api with a dynamic parameter and a query parameter
async def get_by_catageory(book_author:str, category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and book.get("catagory").casefold() == category.casefold():
            book_to_return.append(book)
            
    return book_to_return
        

# POST METHOD
@app.post("/books/new-book/")
async def create_book(new_book= Body()):
    BOOKS.append(new_book)