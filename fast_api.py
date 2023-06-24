from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str] = None

app=FastAPI()

@app.get("/")

def home():
    return {"Data":"Test"}

@app.get("/about")

def about():
    return {"Data":"About"}


inventory = {
1: {
"name": "Milk",
"price": 3.99,
"brand": "Regular"
}
}
@app.get("/get-item/{item_id}")
def get_item(item_id: int= Path(description="The ID")):
    return inventory[item_id]

@app.post("/create-item/{item_id}")

def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return {"Error":"Item already exists"}
    # inventory[item_id]={"name":item.name,"price":item.price,"brand":item.brand}
    inventory[item_id]=item
    return inventory[item_id]
