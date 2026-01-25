from app.repository.crud_users import create_user, read_user
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemes.schemes_module import User
from app.core.security import hash_password, verify_password


def create_user_service(db: Session, user: User):
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    return create_user(db, user)

def read_user_service(db: Session, user: User):
    user_db = read_user(db, user)
    if not verify_password(user.password, user_db.password):
        return HTTPException(status_code=404, detail='Password does not match')
    return user_db