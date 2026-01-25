from sqlalchemy.orm import Session
from app.models.models_module import UserTable
from app.schemes.schemes_module import User

def create_user(db: Session, user: User):
    user_db = UserTable(email=user.email, password=user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def read_user(db: Session, user: User):
    return db.query(UserTable).filter(UserTable.email == user.email).first()