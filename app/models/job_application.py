from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base

class JobApplication(Base):

    __tablename__ = "job application"
    
    id = Column(Integer, primary_key=True, index =True)
    company = Column(String, index=True)
    position = Column(String)
    status = Column(String, default="applied")
    applied_date = Column(Date)
    notes = Column(String, default="")
    