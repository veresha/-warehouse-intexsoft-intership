from sqlalchemy.orm import Session

from src.app.db_worker import get_item_by_id
from src.app.models.models import Item
from src.app.models.schemas import ItemSchema


def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: ItemSchema):
    _item = Item(name=item.name, count=item.count, uuid=item.uuid)
    db.add(_item)
    db.commit()
    db.refresh(_item)


def remove_item(db: Session, item_id: int):
    _item = get_item_by_id(db=db, item_id=item_id)
    db.delete(_item)
    db.commit()


def update_item(db: Session, item_id: int, name: str, count: int, uuid: int):
    _item = get_item_by_id(db=db, item_id=item_id)

    _item.name = name
    _item.count = count
    _item.uuid = uuid

    db.commit()
    db.refresh(_item)
    return _item
