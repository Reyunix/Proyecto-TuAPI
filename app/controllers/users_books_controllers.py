from app.repositories.users_books_repo import add_book_to_user, get_user_books, delete_user_book, get_book_users
from fastapi import HTTPException, status
from sqlmodel import Session
from app.models.users_books import UserBook
from app.models.books import Book
from app.models.users import User

# Añadir libro a usuario
def fetch_add_book_to_user(*,db: Session, user_id: int, book_id=str) -> UserBook | None:    
    try:    
        user_book = add_book_to_user(db=db, user_id=user_id, book_id=book_id)   
        if user_book:
            return user_book        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User or Book not found")
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))

# Obtener libros de un usuario
def fetch_get_user_books(*,db:Session, user_id: int) -> list[Book]:
    user_books = get_user_books(db=db, user_id=user_id)
    if user_books is not None:       
        return user_books
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# Eliminar libro de usuario
def fetch_delete_user_book(*,db:Session, user_id:int, book_id:str):
    deleted_book = delete_user_book(db=db, user_id=user_id, book_id=book_id)
    if deleted_book:
        return "Book deleted correctly"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not existing relationship")

# Obtener usuarios que tienen un libro
def fetch_get_book_users(*,db:Session, book_id: str) -> list[User]:
    book_users = get_book_users(db=db, book_id=book_id)
    if book_users is not None:       
        return book_users
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
