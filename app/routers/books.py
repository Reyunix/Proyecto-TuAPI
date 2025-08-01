# Importamos lo necesario de FastAPI y otros módulos del proyecto
from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session
from app.schemas.books import BookBasicSchema, DictResponseSchema
from app.models.books import Book
from app.db.database import get_session
from app.controllers.books_controllers import (
    fetch_create_book, fetch_get_books, fetch_get_book_by_id, fetch_delete_book
)
import json
from typing import Optional
from app.auth.authorization import authenticate

# Creamos un router para los endpoints de libros
router = APIRouter(prefix="/books", tags=["Books"])

# Endpoint para obtener todos los libros (con filtro opcional por categoría)
@router.get("", description="Get all books")
async def read_books(category: Optional[str] = Query(None), session: Session = Depends(get_session)) -> DictResponseSchema:
    all_books = fetch_get_books(db=session, category=category)
    return {
        "success": True,
        "data": all_books
    }

# Endpoint para obtener un libro por su ID
@router.get("/{book_id}", description="Ask for an book by its ID")
async def read_book_by_id(book_id: str, session: Session = Depends(get_session)) -> DictResponseSchema:
    book = fetch_get_book_by_id(db=session, book_id=book_id)
    return {
        "success": True,
        "data": book
    }

# Endpoint para crear un libro (requiere autenticación)
@router.post("", description="Create a new book", status_code=status.HTTP_201_CREATED)
async def create_book(
    newBook: BookBasicSchema,
    session: Session = Depends(get_session),
    username: str = Depends(authenticate)
) -> DictResponseSchema:
    # Convertimos listas y URL a strings para guardar en la base de datos
    newBook.authors = json.dumps(newBook.authors)
    newBook.categories = json.dumps(newBook.categories)
    newBook.imageLinks = str(newBook.imageLinks)

    # Convertimos el esquema en modelo
    newBook = newBook.model_dump(exclude_unset=True)
    newBook = Book(**newBook)

    # Llamamos al controlador para crear el libro
    created_book = fetch_create_book(db=session, new_book=newBook)
    return {
        "success": True,
        "username": username,
        "data": created_book
    }

# Endpoint para eliminar un libro (requiere autenticación)
@router.delete("/{bookId}", description="Delete an book by its ID")
async def delete_book(
    bookId: str,
    session: Session = Depends(get_session),
    username: str = Depends(authenticate)
) -> DictResponseSchema:
    book = fetch_delete_book(book_id=bookId, db=session)
    return {
        "success": True,
        "username": username,
        "data": book
    }
