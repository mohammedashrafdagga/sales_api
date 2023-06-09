from database import engine, SessionLocal, Base
from models import User, Product, Sales

# create all table in database
Base.metadata.create_all(bind=engine)


# get db
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
