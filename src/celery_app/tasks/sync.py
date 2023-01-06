from typing import List, Dict, Union

from src.celery_app.main import app
from src.main import get_info


@app.task(name='get_info', queue="warehouse_queue")
def warehouse_task(items: List[Dict[str, Union[str, int]]]):
    item_uuid = items[0].get('id')
    item_quantity = items[0].get('quantity')

    result = get_info(item_uuid, item_quantity)

    if not result:
        return [{"id": item_uuid, "status": "Not enough"}]
    return [{"id": item_uuid, "status": "Success"}]
