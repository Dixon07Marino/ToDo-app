from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os, jwt

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

def generate_token(id_user: int) -> str:
    payload = {
        'id': id_user,
        'exp': datetime.now(timezone.utc) + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def validate_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms='HS256')