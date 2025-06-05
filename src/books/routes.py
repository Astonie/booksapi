from fastapi import APIRouter
from fastapi import HTTPException, status
from src.books.schemas import Book, BookUpdateModel
from typing import List
from src.books.books_data import books


books_router = APIRouter()


@books_router.get("/", response_model=List[Book])
async def get_books():
    return books


@books_router.get('/{book_id}')
def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')

@books_router.post('/', status_code=status.HTTP_201_CREATED)
def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@books_router.put('/{book_id}')
def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title or book['title']
            book['author'] = book_update_data.author or book['author']
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')


@books_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
