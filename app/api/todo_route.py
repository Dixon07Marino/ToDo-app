from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemes.schemes_module import Task
from app.services.todo_service import validate_tasks, validate_task, validate_created_task, validate_updated_task, validate_deleted_task

router = APIRouter()

@router.get('/')
async def greet():
    return {'msg': 'Hello, from backend!'}

@router.get('/tasks')
async def get_tasks(db: Session = Depends(get_db)):
    return validate_tasks(db)

@router.get('/tasks/{id_task}')
async def get_task(id_task: int, db: Session = Depends(get_db)):
    return validate_task(db, id_task)

@router.post('/tasks', status_code=201)
async def add_task(task: Task ,db: Session = Depends(get_db)):
    return validate_created_task(db, task)

@router.put('/tasks/{id_task}')
async def update_task(id_task: int, task: Task, db: Session = Depends(get_db)):
    return validate_updated_task(db, id_task, task)

@router.delete('/tasks/{id_task}')
async def delete_task(id_task: int, db: Session = Depends(get_db)):
    return validate_deleted_task(db, id_task)