from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.database import get_session
from app.controllers.users_books_controllers import fetch_add_book_to_user, fetch_get_user_books, fetch_delete_user_book, fetch_get_book_users
from app.auth.authorization import authenticate

# Creamos el router para los endpoints de relaciones entre usuarios y libros
router = APIRouter(tags=["User books"])

# Obtener todos los libros que tiene un usuario
@router.get("/user/{user_id}/books")
async def read_user_books(user_id: int, session:Session = Depends(get_session)):
    user_books = fetch_get_user_books(db=session, user_id= user_id)
    return user_books

# Añadir un libro a un usuario (requiere autenticación)
@router.post("/user/{user_id}/books/{book_id}")
async def add_book_to_user(user_id: int, book_id:str, session:Session = Depends(get_session), username: str = Depends(authenticate)):
    user_book = fetch_add_book_to_user(user_id=user_id, book_id=book_id, db=session)
    
    return {"success": True,
            "username": username,
            "data": user_book
            }

# Eliminar un libro de un usuario (requiere autenticación)
@router.delete("/user/{user_id}/books/{book_id}")
async def delete_user_book(user_id: int, book_id:str, session:Session = Depends(get_session), username: str = Depends(authenticate)):
    deleted_book = fetch_delete_user_book(user_id=user_id, book_id=book_id, db=session)
    
    return {"success": True,
            "username": username,
            "data": deleted_book
            }

# Obtener todos los usuarios que tienen un libro
@router.get("/book/{book_id}/users")
async def read_book_users(book_id: str, session:Session = Depends(get_session)):
    book_books = fetch_get_book_users(db=session, book_id= book_id)
    return book_books
