from sqlmodel import Session, select
from app.models.users import User
from app.models.books import Book
from app.models.users_books import UserBook

# Crea una relación entre un usuario y un libro si no existe ya. Si existe devuelve un error
def add_book_to_user(*, user_id: int, book_id: str, db: Session) -> UserBook | None:
    existing_relationship = db.exec(
        select(UserBook).where(UserBook.user_id == user_id, UserBook.book_id == book_id)
    ).first()
    
    if existing_relationship:
        raise ValueError("User already has this book")
    
    user = db.exec(select(User).where(User.id == user_id)).first()
    book = db.exec(select(Book).where(Book.id == book_id)).first()
    
    if not user or not book:
        return None

    user_book = UserBook(user_id=user.id, book_id=book.id)
    db.add(user_book)
    db.commit()
    db.refresh(user_book)
    
    return user_book

# Devuelve todos los libros asociados a un usuario
def get_user_books(*, user_id: int, db=Session) -> list[Book]:
    user = db.exec(select(User).where(User.id == user_id)).first()
    if user is None:
        return None
    return user.books

# Elimina la relación entre un usuario y un libro si existe
def delete_user_book(*, user_id: int, book_id: str, db: Session):
    existing_relationship = db.exec(
        select(UserBook).where(UserBook.user_id == user_id, UserBook.book_id == book_id)
    ).first()
    
    if existing_relationship:
        db.delete(existing_relationship)
        db.commit()
        return existing_relationship
    
    return None

# Devuelve todos los usuarios que tienen un libro determinado
def get_book_users(*, book_id: str, db: Session) -> list[User]:
    book = db.exec(select(Book).where(Book.id == book_id)).first()
    
    if book is None:
        return None
    
    return book.users
