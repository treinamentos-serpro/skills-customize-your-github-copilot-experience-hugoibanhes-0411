from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    raise NotImplementedError("Complete this endpoint in Task 1")


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    raise NotImplementedError("Complete this endpoint in Task 2")


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_data: BookCreate) -> Book:
    raise NotImplementedError("Complete this endpoint in Task 3")