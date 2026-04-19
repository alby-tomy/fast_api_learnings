from fastapi import FastAPI

app = FastAPI() # this allow uvicorn to identify that we are creating a new application of fastAPI and this will import all of the resources


@app.get("/api-endpoint") # this is the decorator which will allow us to define the type of request method and the path of the api
async def first_api():
    return {"message": "Hello World!"}