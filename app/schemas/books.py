from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Any
from datetime import date

# Esquema de entrada para crear o recibir datos de un libro desde la API
class BookBasicSchema(BaseModel):
    title: str                                # Título del libro
    subtitle: Optional[str] = None            # Subtítulo (opcional)
    authors: List[str]                        # Lista de autores
    categories: List[str] = None              # Lista de categorías (opcional)
    publisher: Optional[str] = None           # Editorial (opcional)
    publishedDate: Optional[date] = None      # Fecha de publicación (opcional)
    pageCount: int                            # Número de páginas
    imageLinks: Optional[HttpUrl] = None      # Enlace de imagen (opcional, debe ser URL válida)
    language: str                             # Idioma del libro
    isbn_13: str = None                       # ISBN-13 (opcional)
    isbn_10: Optional[str] = None             # ISBN-10 (opcional)

# Esquema de respuesta general para estructurar respuestas JSON
class DictResponseSchema(BaseModel):
    success: bool     # Indica si la operación fue exitosa
    data: Any         # Contiene los datos devueltos (puede ser cualquier tipo)
