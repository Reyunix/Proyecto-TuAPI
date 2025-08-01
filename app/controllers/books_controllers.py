# Importamos lo necesario
from fastapi import HTTPException, status  # Para lanzar errores HTTP
from app.repositories import books_repo    # Funciones para interactuar con la base de datos de libros
from sqlmodel import Session               # Conexión con la base de datos
from app.models.books import Book          # Modelo del libro
from app.models.users_books import UserBook  # Modelo de la relación entre usuarios y libros
from app.utils.custom_errors import RelationalUserBookError  # Error personalizado

# Crear un nuevo libro
def fetch_create_book(db: Session, new_book: Book) -> str:
    try:
        book = books_repo.create_new_book(db, new_book)  # Intenta crear el libro
        return book  # Si va bien, lo devuelve
    except ValueError as error:
        # Si hay un error (por ejemplo, el libro ya existe), lanza un error 409
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))

# Obtener todos los libros (con opción de filtrar por categoría)
def fetch_get_books(*, db, category: str = None) -> list[Book]:
    all_books = books_repo.get_books(db=db, category=category)  # Trae los libros
    return all_books

# Buscar un libro por su ID
def fetch_get_book_by_id(db, book_id) -> Book | None:
    book = books_repo.get_book_by_id(db, book_id)
    if book:
        return book  # Si lo encuentra, lo devuelve
    # Si no lo encuentra, lanza un error 404
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# Borrar un libro por su ID
def fetch_delete_book(db: Session, book_id: int) -> str | None:
    try:
        book = books_repo.delete_book(db=db, book_id=book_id)
        if book:
            return book  # Si se borra bien, lo devuelve
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    except RelationalUserBookError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))

