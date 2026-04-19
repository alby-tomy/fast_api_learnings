# FastAPI: Complete Guide from Basics to Advanced

## 1. Introduction to FastAPI

FastAPI is a modern, fast web framework for building APIs with Python. It's built on Starlette and Pydantic, offering automatic documentation and type hints.

### Why FastAPI?
- **Fast Performance**: One of the fastest Python frameworks
- **Easy to Learn**: Intuitive syntax for beginners
- **Automatic Docs**: Built-in Swagger UI and ReDoc
- **Type Safety**: Uses Python type hints for validation

---

## 2. Getting Started

### Installation
```bash
pip install fastapi uvicorn
```

### First API
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

Run with: `uvicorn main:app --reload`

---

## 3. Core Concepts

### Path Parameters
```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

### Query Parameters
```python
@app.get("/users/")
def get_users(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### Request Body
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

---

## 4. HTTP Methods

- `@app.get()` - Retrieve data
- `@app.post()` - Create data
- `@app.put()` - Update entire object
- `@app.patch()` - Partial update
- `@app.delete()` - Remove data

---

## 5. Advanced Topics

### Middleware
```python
from fastapi.middleware import Middleware

@app.middleware("http")
async def add_process_time_header(request, call_next):
    response = await call_next(request)
    return response
```

### Error Handling
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    return {"item_id": item_id}
```

### Async Operations
```python
@app.get("/async-items/")
async def get_async_items():
    # Perform async operations
    return {"items": []}
```

---

## 6. Best Practices

- Use descriptive endpoint names
- Validate input with Pydantic models
- Handle errors gracefully
- Use async for I/O operations
- Document with docstrings

## 7. Fast API documentation
- url : https://fastapi.tiangolo.com/
