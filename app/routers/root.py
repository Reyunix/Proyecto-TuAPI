from fastapi import APIRouter


router = APIRouter()

# Endpoint raiz de la api, te muestra las rutas más relevantes
@router.get("/", description="Root path")
def read_root():
    return {
    "success": True,
    "data": {
        "/": "Root of the API. Shows available endpoints.",
        "/users": "GET: List all users (optional filter by 'is_active'), POST: Create new user",
        "/users/{user_id}": "GET: Get user by ID, PUT: Modify user by ID, DELETE: Delete user by ID",
        "/books": "GET: List all books (optional filter by 'category'), POST: Create new book",
        "/books/{book_id}": "GET: Get book by ID, DELETE: Delete book by ID",
        "/users-books/users/{user_id}/books": "GET: Get all books for a given user",
        "/users-books/books/{book_id}/users": "GET: Get all users for a given book",
        "/users-books/assign": "POST: Assign a book to a user",
        "/users-books/remove": "DELETE: Remove a book from a user"
    }
}