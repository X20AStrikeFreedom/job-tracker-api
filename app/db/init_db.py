from app.db.database import Base, engine
from app.models import job_application

Base.metadata.create_all(bind=engine)
print("Database created!")
