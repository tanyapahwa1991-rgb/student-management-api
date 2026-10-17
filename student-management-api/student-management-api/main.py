"""Application entry point for the Student Management API."""
from fastapi import FastAPI
from app.database import Base, engine
from app.routes.students import router as students_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description=(
        "A mini-internship project demonstrating Create, Read, Update and Delete "
        "(CRUD) operations for student records using FastAPI and SQLite. "
        "Use the interactive documentation to test the endpoints."
    ),
    version="1.0.0",
)

app.include_router(students_router)


@app.get("/", tags=["General"])
def root():
    return {
        "message": "Welcome to the Student Management API.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["General"])
def health_check():
    return {"status": "ok"}
