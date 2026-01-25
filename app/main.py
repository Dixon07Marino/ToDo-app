from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import todo_route
from app.api import auth_route
import app.models.models_module as models_module
from app.db.database import engine

app = FastAPI(
    title="To-do API",
    docs_url="/api/docs",       
    redoc_url="/api/redoc",        
    openapi_url="/api/openapi.json"
)

models_module.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_route.router, prefix='/api')
app.include_router(auth_route.router, prefix='/api')