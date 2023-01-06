from sqlalchemy.orm import Session
from src.app.models import models
from src.app.models.database import engine, SessionLocal
from src.app.models.models import Item
from src.celery_app.tasks.sync import warehouse_task

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_item_by_uuid(db: Session, uuid: int):
    return db.query(Item).get(Item.uuid == uuid)


def get_info(uuid: int, quantity: int):
    # db = get_db()
    db = SessionLocal()
    item = get_item_by_uuid(db, uuid)
    db.close()
    if quantity >= item.count:
        return True
    else:
        return False
