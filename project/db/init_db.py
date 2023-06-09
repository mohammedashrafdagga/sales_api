from project.db.database import engine, SessionLocal, Base
from project.apps.authenticate.models import User
from project.apps.product.models import Product
from project.apps.sales.models import Sales

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
