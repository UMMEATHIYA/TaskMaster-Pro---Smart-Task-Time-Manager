from fastapi import FastAPI
from .database import Base, engine
from .routes import tasks

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskMaster Pro – Smart Task Manager")

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
