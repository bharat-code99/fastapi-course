from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

posts = [
    {"id": 1, "title": "Post 1"},
    {"id": 2, "title": "Post 2"}
]

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def read_root():
    return "<h1>Awesome FastAPI</h1>"

@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}