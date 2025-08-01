from fastapi import HTTPException, status
from app.repositories import users_repo
from app.models.users import User
from sqlmodel import Session

# Obtener usuarios
def fetch_users(*, db:Session, is_active: bool = None) -> list[User]:
    book = users_repo.get_users(db=db, is_active=is_active)  
    return book

# Buscar usuario por ID
def fetch_user_by_id(*, db:Session, user_id: int) -> User | None:    
    user = users_repo.get_user_by_id(db=db,user_id=user_id)    
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# Eliminar usuario
def fetch_delete_user(*, db:Session, user_id: int) -> str | None:    
    user = users_repo.delete_user(db=db, user_id=user_id)    
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# Actualizar usuario
def fetch_update_user(*, db:Session, user_id: int, modify_user_data) -> str | None:
    try:
        user = users_repo.modify_user(db=db, user_id=user_id, modify_user_data=modify_user_data)    
        if user:
            return user
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))

# Crear usuario
def fetch_create_user(*, db: Session, new_user: User) -> str:   
    try: 
        created_user = users_repo.create_new_user(db=db, newUser=new_user)
        return created_user
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))
