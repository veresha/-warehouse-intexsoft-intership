from sqlalchemy.orm import Session
from src.app.models.database import engine, SessionLocal
from src.app.models.models import Item


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def get_item_by_uuid(db: Session, uuid: int):
    return db.query(Item).get(Item.uuid == uuid)


def get_db_info(uuid: int, quantity: int):
    with get_db() as db:
        item = get_item_by_uuid(db, uuid)
    return quantity >= item.count
