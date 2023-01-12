from sqlalchemy.orm import Session
from src.app.models.database import engine, SessionLocal
from src.app.models.models import Item


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
    return quantity >= item.count
