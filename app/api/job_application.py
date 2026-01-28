from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.job_application import JobApplication, JobApplicationCreate, JobApplicationUpdate
from app.db.database import get_db
from app.crud.job_application import get_all_applications, get_application, create_application, update_application, delete_application

router = APIRouter(prefix="/applications", tags=["applications"])

@router.get("/", response_model=List[JobApplication])
def read_applications(db: Session = Depends(get_db)):
    return get_all_applications(db)

@router.get("/{application_id}", response_model=JobApplication)
def read_application(application_id: int, db: Session = Depends(get_db)):
    app_obj = get_application(db, application_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj
    
@router.post("/", response_model=JobApplication)
def create_new_application(application: JobApplication, db:Session = Depends(get_db)):
    return create_application(db, application)
 
@router.put("/{application_id}", response_model=JobApplication)
def update_existing_application(application_id: int, updates: JobApplicationUpdate, db: Session = Depends(get_db)):
    app_obj = update_application(db, application_id, updates)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj

@router.delete("/{application_id}", response_model=JobApplication)
def delete_existing_application(application_id: int, db: Session = Depends(get_db)):
    app_obj = delete_application(db, application_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj
    