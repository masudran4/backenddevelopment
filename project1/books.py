from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"id": 1, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 2, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 3, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 4, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 5, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 6, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 7, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 8, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 9, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 10, 'title': 'Title one', 'author': 'author one', 'category': 'science'}
]


@app.get("/hello")
async def say_hello():
    return {"message": "Hello Masud"}


@app.get("/books")
async def get_books():
    return BOOKS


@app.get("/books/{id}")
async def get_book(id: int):
    for book in BOOKS:
        if id == book['id']:
            return book
