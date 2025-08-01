from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, timezone
from app.models.users_books import UserBook


# Modelo de la tabla de usuarios para la base de datos
class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    password_hash: str = Field(nullable=False)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_active: bool = Field(default=True)
    
    # Relación muchos a muchos con libros usando la tabla intermedia UserBook
    books: Optional[List["Book"]] = Relationship(back_populates="users", link_model=UserBook) # type: ignore
    

class UserModifyModel(SQLModel, table = False):    
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    
    class Config:
        from_attributes = True
        
# No he llegado a implementar esta clase       
class UserPasswordUpdate(SQLModel, table=False):
    password_hash: str