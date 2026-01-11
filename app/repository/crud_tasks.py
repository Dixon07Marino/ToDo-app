from sqlalchemy.orm import Session
from app.models.models_module import TaskTable
from app.schemes.schemes_module import Task

def read_tasks(db: Session):
    return db.query(TaskTable).all()

def read_task(db: Session, id_task: int):
    return db.query(TaskTable).filter(TaskTable.id == id_task).first()

def create_task(db: Session, task: Task):
    db_task = TaskTable(name=task.name)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def change_task(db: Session, id_task: int, task: Task):
    db_task = db.query(TaskTable).filter(TaskTable.id == id_task).first()
    db_task.name = task.name
    db.commit()
    db.refresh(db_task)
    return db_task

def remove_task(db: Session, id_task: int):
    db_task = db.query(TaskTable).filter(TaskTable.id == id_task).first()
    db.delete(db_task)
    db.commit()
    return db_task