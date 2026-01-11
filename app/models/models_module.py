from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class TaskTable(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250))