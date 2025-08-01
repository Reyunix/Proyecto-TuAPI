from pydantic import BaseModel, Field
from typing import Optional

# Esquema para crear un nuevo usuario (entrada de datos)
class UserBasicSchema(BaseModel):
    username: str = Field(max_length=50, min_length=3)                   # Nombre de usuario entre 3 y 50 caracteres
    email: str = Field(max_length=50, min_length=4)                      # Email entre 4 y 50 caracteres
    password_hash: str = Field(min_length=8, max_length=40, example="string") 
    # Contraseña en texto plano o hasheada (entre 8 y 40 caracteres), ejemplo mostrado en Swagger
    first_name: Optional[str] = None                                     # Nombre (opcional)
    last_name: Optional[str] = None                                      # Apellido (opcional)

# Esquema para actualizar/modificar datos de un usuario
class ModifyUserDataSchema(BaseModel):
    username: Optional[str] = None       # Todos los campos son opcionales
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
