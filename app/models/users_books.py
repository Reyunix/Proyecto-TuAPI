from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone

# Tabla intermedia para relacionar usuarios y libros
class UserBook(SQLModel, table=True):
    __tablename__ = "user_books"
    
    user_id: int = Field(foreign_key="users.id", primary_key=True)
    book_id: int = Field(foreign_key="books.id", primary_key=True)
    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))