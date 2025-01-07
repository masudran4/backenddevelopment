from pydantic import BaseModel, Field
from datetime import datetime

from fastapi import FastAPI, Path, Query, HTTPException, status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_data: str

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: int = Field(default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6, default=1)
    published_date: str = Field(min_length=10)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book title",
                "author": "Book author",
                "description": "Book description",
                "rating": 5,
                "published_date": "2024-12-12"
            }
        }
    }


BOOKS = [
    Book(1, "Programming Deep part 1", "alom", "Very Basic Understanding", 4, "2020-12-12"),
    Book(2, "Programming Deep part 2", "alom", "Very Basic Understanding", 5, "2020-12-12"),
    Book(3, "Programming Deep part 3", "tayeb", "Very Basic Understanding", 4, "2020-12-12"),
    Book(4, "Programming Deep part 4", "Rana", "Very Basic Understanding", 5, "2020-12-12"),
    Book(5, "Programming Deep part 5", "Rana", "Very Basic Understanding", 4, "2020-12-12")
]


def get_new_book_id(book):
    if len(BOOKS) == 0:
        book.id = 1
    else:
        book.id = BOOKS[-1].id + 1
    return book


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/books/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(new_book: BookRequest):
    BOOKS.append(get_new_book_id(Book(**new_book.model_dump())))


@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def read_book(id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(404, "Book not found with id {id}".format(id=id))


@app.get("/books/by_date/", status_code=status.HTTP_200_OK)
async def get_book_by_published_date(published_date: str):
    book_to_return = []
    for book in BOOKS:
        if datetime.strptime(book.published_date, '%Y-%m-%d') >= datetime.strptime(published_date, '%Y-%m-%d'):
            book_to_return.append(book)
    return book_to_return


@app.get("/books/")
async def get_book(rating: int = Query(gt=0, lt=len(BOOKS)),author: str = Query(min_length=2,default=None)):
    book_to_return = []
    for book in BOOKS:
        if book.rating >= rating:
            book_to_return.append(book)
    if author:
        for book in BOOKS:
            if book.author == author:
                book_to_return.append(book)
    return book_to_return


@app.put("/books/update_book")
async def update_book(new_book: BookRequest):
    for i in range(0, len(BOOKS)):
        if BOOKS[i].id == new_book.id:
            BOOKS[i] = new_book
            return
    raise HTTPException(404, "Book not found with id {id}".format(id=new_book.id))


@app.delete("/books/{id}")
async def delete_book(id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == id:
            BOOKS.remove(book)
            return
    raise HTTPException(404,detail="Book not found with id {id}".format(id=id))
