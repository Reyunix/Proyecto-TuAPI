from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import uuid4
import json
from app.models.users_books import UserBook

class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: str = Field(default_factory = lambda: str(uuid4()).replace("-","")[0:20], index=True, primary_key=True ) # Cambio el formato de las uuid y limito su tamaño a 20 caracteres por legibilidad
    title: str = Field(index=True)
    subtitle: Optional[str] = None
    authors: str
    categories: str = None
    publisher: Optional[str] = None
    publishedDate: Optional[str] = None
    pageCount: int
    imageLinks: Optional[str] = None
    language: str
    isbn_13: str = Field(unique=True, index=True)
    isbn_10: Optional[str] = None
    # Para la relación con libros
    users: Optional[List["User"]] = Relationship(back_populates="books", link_model=UserBook) # type: ignore
    
    # Métodos para transformar los string a su respectivo tipo de dato
    def get_authors(self) -> list[str]:
        return json.loads(self.authors) if self.authors else []
    
    def get_categories(self) -> list[str]:
        return json.loads(self.categories) if self.categories else []
    
    def get_imageLinks(self) -> dict:
        return json.loads(self.imageLinks) if self.imageLinks else {}