from fastapi import FastAPI
from app.api import job_application

app = FastAPI()

app.include_router(job_application.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
    