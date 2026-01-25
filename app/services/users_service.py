from app.repository.crud_users import create_user, read_user
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemes.schemes_module import User
from app.core.security import hash_password, verify_password
from app.core.auth import generate_token, validate_token

def create_user_service(db: Session, user: User):
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    return create_user(db, user)

def read_user_service(db: Session, user: User):
    user_db = read_user(db, user)
    if not verify_password(user.password, user_db.password):
        return HTTPException(status_code=404, detail='Password does not match')
    token: str = generate_token(user_db.id)
    return {'msg': 'you are logged...', 'token': token}

def read_token_service(token: str):
    payload = validate_token(token)
    id_user = payload.get('id')
    if not id_user:
        return HTTPException(status_code=404, detail='Token invalido')
    return {'msg': f'Usuarion con id: {id_user} ha ingresado con exito'}