from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.todo_route import router
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

app.include_router(router, prefix='/api')