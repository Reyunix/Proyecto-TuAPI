from sqlmodel import Session, select
from app.models.users import User, UserModifyModel


# Obtener todos los usuarios, con filtro opcional por estado activo
def get_users(*, db: Session, is_active: bool = None) -> list[User]:
    query = select(User)
    if is_active is not None:
        query = query.where(User.is_active == is_active)
    return db.exec(query).all()


# Obtener un usuario por su ID
def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)


# Eliminar un usuario por ID
def delete_user(db: Session, user_id: int) -> str | None:
    user = db.get(User, user_id)
    if user:
        db.delete(user)
        db.commit()
        return "User deleted successfully"
    return None


# Modificar un usuario, validando duplicados en username y email
def modify_user(
    db: Session, user_id: int, modify_user_data: UserModifyModel
) -> str | None:
    user = db.get(User, user_id)
    if not user:
        return None

    if modify_user_data.username:
        existing_user = db.exec(
            select(User).where(
                User.username == modify_user_data.username, User.id != user.id
            )
        ).first()
        if existing_user:
            raise ValueError("An user with the same username already exists")

    if modify_user_data.email:
        existing_email = db.exec(
            select(User).where(User.email == modify_user_data.email, User.id != user.id)
        ).first()
        if existing_email:
            raise ValueError("An user with the same email already exists")

    for key, value in modify_user_data.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)
    return "User updated successfully"


# Crear nuevo usuario, validando duplicados en username y email
def create_new_user(db: Session, newUser: User) -> str:
    existing_user = db.exec(
        select(User).where(User.username == newUser.username)
    ).first()
    if existing_user:
        raise ValueError("An user with the same username already exists")

    existing_email = db.exec(select(User).where(User.email == newUser.email)).first()
    if existing_email:
        raise ValueError("An user with the same email already exists")

    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return "User create successfully"
