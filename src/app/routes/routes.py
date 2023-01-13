from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.models.schemas import Response, RequestItem, ItemSchema
from src.app.db_worker import get_db
from src.app.services import crud

router = APIRouter()


@router.post("/add_items")
async def add_items(db: Session = Depends(get_db)):
    item = ItemSchema()
    for i in range(10):
        item.name = f'IPhone {i}'
        item.count = f'IPhone {i} count'
        item.uuid = 2323
        await create_item(db, item=item)
    return Response(status="Ok",
                    code="200",
                    message="Items created successfully").dict(exclude_none=True)


@router.post("/create")
async def create_item(request: RequestItem, db: Session = Depends(get_db)):
    crud.create_item(db, item=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Item created successfully").dict(exclude_none=True)


@router.get("/")
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _items = crud.get_item(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)


@router.patch("/update")
async def update_item(item_id: int, name: str, count: int, uuid: int, db: Session = Depends(get_db)):
    _item = crud.update_item(db, item_id=item_id, name=name, count=count, uuid=uuid)
    return Response(status="Ok", code="200", message="Success update data", result=_item)


@router.delete("/delete")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    _item = crud.remove_item(db, item_id=item_id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


