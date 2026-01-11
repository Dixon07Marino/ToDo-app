from app.repository.crud_tasks import read_tasks, read_task, create_task, change_task, remove_task
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemes.schemes_module import Task

def validate_tasks(db: Session):
    try:
        tasks_data = read_tasks(db)
        if not tasks_data:
            return HTTPException(status_code=404, detail='There are no tasks yet')
        return tasks_data
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Something went wrong... Error: {e}')
    
def validate_task(db: Session, id_task: int):
    try:
        task_data = read_task(db, id_task)
        if not task_data:
            return HTTPException(status_code=404, detail='This task does not exist...')
        return task_data
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Something went wrong... Error: {e}')

def validate_created_task(db: Session, task: Task):
    try:
        task_data = create_task(db, task)
        if not task_data:
            return HTTPException(status_code=404, detail='Task couldnt be created...')
        return task_data
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Something went wrong... Error: {e}')

def validate_updated_task(db: Session, id_task: int, task: Task):
    try:
        task_data = change_task(db, id_task, task)
        if not task_data:
            return HTTPException(status_code=404, detail='Task couldnt be updated...')
        return task_data
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Something went wrong... Error: {e}')

def validate_deleted_task(db: Session, id_task: int):
    try:
        task_data = remove_task(db, id_task)
        if task_data is None:
            return {'msg': 'Task was deleted'}
        return HTTPException(status_code=404, detail='Task couldnt be deleted...')
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Something went wrong... Error: {e}')