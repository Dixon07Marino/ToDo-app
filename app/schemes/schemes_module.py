from pydantic import BaseModel, EmailStr

class Task(BaseModel):
    name: str

class User(BaseModel):
    email: EmailStr
    password: str