from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemes.schemes_module import User
from app.services.users_service import create_user_service, read_user_service, read_token_service

token_context = OAuth2PasswordBearer(tokenUrl='/api/login')
router = APIRouter()

@router.post('/register')
async def register_user(user: User, db: Session = Depends(get_db)):
    return create_user_service(db, user)

@router.post('/login')
async def login_user(user: User, db: Session = Depends(get_db)):
    return read_user_service(db, user)

@router.get('/protected')
async def protected(token: str = Depends(token_context)):
    return read_token_service(token)