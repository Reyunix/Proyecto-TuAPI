from sqlmodel import SQLModel, Session, create_engine
from app.models import users, books


# Configuramos la url de la base de datos
db_name = "database.db"
db_url = f"sqlite:///app/db/{db_name}"

# Configuramos el motos de base de datos para crear las sesiones
engine = create_engine(db_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session   
        
# Nos aseguramos de que la función se ejecute sólo si se hace desde este archivo directamente
if __name__ == "__main__":    
    SQLModel.metadata.create_all(engine)