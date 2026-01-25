from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemes.schemes_module import User
from app.services.users_service import create_user_service, read_user_service
router = APIRouter()

@router.post('/register')
async def register_user(user: User, db: Session = Depends(get_db)):
    return create_user_service(db, user)

@router.post('/login')
async def login_user(user: User, db: Session = Depends(get_db)):
    return read_user_service(db, user)