from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"id": 1, 'title': 'Title one', 'author': 'rana', 'category': 'science'},
    {"id": 2, 'title': 'Title one', 'author': 'rana', 'category': 'science'},
    {"id": 3, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 4, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 5, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 6, 'title': 'Title one', 'author': 'author one', 'category': 'science'},
    {"id": 7, 'title': 'Title one', 'author': 'alom', 'category': 'science'},
    {"id": 8, 'title': 'Title one', 'author': 'alom', 'category': 'science'},
    {"id": 9, 'title': 'Title one', 'author': 'rana', 'category': 'science'},
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


@app.get("/books/")
async def get_books(author: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'] == author:
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"book_id": new_book['id']}


@app.put("/books/update_book/{id}")
async def update_book(id: int, new_book=Body()):
    for book in BOOKS:
        if book['id'] == id:
            book['title'] = new_book['title']
            book['author'] = new_book['author']
            book['category'] = new_book['category']
            return
    return {"message": "Book not found"}


@app.patch("/books/update_book/{id}")
def update_book(id: int, new_book=Body()):
    for index in range(len(BOOKS)):
        if BOOKS[index]['id'] == id:
            BOOKS[index]['category'] = new_book['category']
            return
    return {"message": "Book not found"}


@app.delete("/books/dalete_book/{id}")
async def delete_book(id: int):
    for index in range(len(BOOKS)):
        if BOOKS[index]['id'] == id:
            del BOOKS[index]
            return
    return {"message": "Book not found"}
