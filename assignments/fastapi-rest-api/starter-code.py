from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de ejemplo
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# Base de datos simulada
items_db: List[Item] = []

@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for idx, db_item in enumerate(items_db):
        if db_item.id == item_id:
            items_db[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, db_item in enumerate(items_db):
        if db_item.id == item_id:
            del items_db[idx]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
