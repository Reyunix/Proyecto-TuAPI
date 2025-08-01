from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
from dotenv import load_dotenv

security = HTTPBasic()
# Cargo el usuario y contraseña desde el .env
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Aquí defino un usuario y contraseña hardcodeada
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = username
    correct_password = password

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

