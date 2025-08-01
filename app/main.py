from fastapi import FastAPI
from app.routers import root, users, books, users_books
# Inicializamos la instancia de FastAPi
app = FastAPI(
    title="UNIX's Library API",
    version="0.0.1",
    description="Proyecto de FastAPI conectada a una base de datos sqlite."
)

# Ruta raíz
app.include_router(root.router)

# Rutas de los recursos 
app.include_router(users.router)
app.include_router(books.router)
app.include_router(users_books.router)


