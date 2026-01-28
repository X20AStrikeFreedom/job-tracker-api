from sqlalchemy.orm import Session
from app.models.job_application import JobApplication
from app.schemas.job_application import JobApplicationCreate, JobApplicationUpdate

def get_all_applications(db:Session):
    return db.query(JobApplication).all()
   
def get_application(db:Session, application_id: int):
    return db.query(JobApplication).filter(JobApplication.id == application_id).first()

def create_application(db: Session, application: JobApplicationCreate):
    db_app = JobApplication(**application.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

def update_application(db:Session, application_id: int, updates: JobApplicationUpdate):
    db_app = db.query(JobApplication).filter(JobApplication.id == application_id).first()
    if not db_app:
        return None

    update_data = updates.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_app, field, value)
    db.commit()
    db.refresh(db_app)
    return db_app
 
def delete_application(db:Session, application_id: int):
    db_app = db.query(JobApplication).filter(JobApplication.id == application_id).first()
    if not db_app:
        return None
    db.delete(db_app)
    db.commit()
    return db_app