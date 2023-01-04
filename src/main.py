from sqlalchemy.orm import Session

from .app.models import models
from .app.models.database import engine, SessionLocal
from .app.models.models import Item

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_items(db: Session):
    return db.query(Item).all()
