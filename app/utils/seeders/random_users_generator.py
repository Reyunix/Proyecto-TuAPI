# Crear libros válidos aleatorios
from sqlmodel import Session
from app.db.database import engine
from faker import Faker
from app.routers.users import fetch_create_user
from app.models.users import User

# Función para generar usuarios aleatorios en modo easy


def create_random_users(quantity: int, session: Session):
    fk = Faker()
    print("-- Generador de usuarios aleatorios --")
 
    for _ in range(quantity):        
        user_data = {
            "username": fk.user_name(),
            "email": fk.email(),
            "password_hash": fk.password(special_chars=True, digits=True, upper_case=True, lower_case=True),
            "first_name": fk.first_name(),
            "last_name": fk.last_name(),
            "is_active": fk.boolean(chance_of_getting_true=75)
            }
        user_data = User(**user_data)
        fetch_create_user(db=session, new_user=user_data)        
    print(f"\n{quantity} usuarios creados correctamente")



if __name__ == "__main__":    
    try:
        quantity = int(input("Cantidad de usuarios: "))
        with Session(engine) as session:         
            create_random_users(quantity, session)
    except ValueError as error:
        print("\nIngresa un número válido\n", error)