from pydantic import BaseModel
from datetime import date
from typing import Optional

class JobApplicationBase(BaseModel):
    company: str
    position: str
    status: Optional[str] = "applied"
    applied_date: date
    notes: Optional[str] = ""
   
class JobApplicationCreate(JobApplicationBase):
    pass

class JobApplicationUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None

class JobApplication(JobApplicationBase):
    id: int
   
class Config:
    orm_mode = True