from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1, 
        "author": "Bharat", 
        "title": "FastAPI is Awesome", 
        "content": "This framework is really easy to use and super fast", 
        "date_posted": "01, Oct, 2026"
    },
    {
        "id": 2, 
        "author": "Jane", 
        "title": "Python is great for Web Development", 
        "content": "Python is great for Web Development, and FastAPI makes it even better", 
        "date_posted": "24, Sep, 2026"
    }
]

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html.j2", context={"posts": posts, "title": "Home Page"})

# @app.get("/output.css", include_in_schema=False)
# def get_stylesheet():
#     return FileResponse("src/output.css", media_type="text/css")

@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}