from sqlmodel import Session, select
from app.models.books import Book
from app.models.users_books import UserBook
from sqlalchemy import or_
from app.utils.custom_errors import RelationalUserBookError

# Recupera todos los libros de la base de datos, con opción de filtrado por categoría (insensible a mayúsculas)
def get_books(*, db: Session, category: str = None) -> list[Book]:
    books = db.exec(select(Book)).all()
    if category is not None:
        books = [book for book in books if category.lower() in book.get_categories()]
    return books

# Crea un nuevo libro en la base de datos si no existe otro con el mismo ID o ISBN
def create_new_book(db: Session, new_book: Book) -> str:
    existing_book = db.exec(
        select(Book).where(
            or_(
                Book.id == new_book.id,
                Book.isbn_13 == new_book.isbn_13,
                Book.isbn_10 == new_book.isbn_10
            )
        )
    ).first()

    if existing_book:
        raise ValueError("This book already exists")
    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return "Book created successfully"

# Busca un libro por su ID primario. Devuelve None si no se encuentra.
def get_book_by_id(db: Session, book_id: str) -> Book | None:
    book = db.get(Book, book_id)
    if book:
        return book
    else:
        return None

# Elimina un libro si no está relacionado con ningún usuario; si lo está, lanza un error personalizado
def delete_book(db: Session, book_id: str) -> str | None:
    book_has_owner = db.exec(select(UserBook).where(UserBook.book_id == book_id)).first()
    if book_has_owner:
        raise RelationalUserBookError("This book is owned by one or more users")
    
    book = db.get(Book, book_id)
    if book:
        db.delete(book)
        db.commit()
        return "Book deleted correctly"
    
    return None
