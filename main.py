from fastapi import FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
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
        "date_posted": "01, Oct, 2026",
    },
    {
        "id": 2,
        "author": "Jane",
        "title": "Python is great for Web Development",
        "content": "Python is great for Web Development, and FastAPI makes it even better",
        "date_posted": "24, Sep, 2026",
    },
    {
        "id": 3,
        "author": "Alex",
        "title": "Getting Started with FastAPI",
        "content": "FastAPI makes it simple to build modern and high-performance APIs",
        "date_posted": "20, Sep, 2026",
    },
    {
        "id": 4,
        "author": "Sarah",
        "title": "Why I Love Python",
        "content": "Python has a clean syntax and a huge ecosystem of useful libraries",
        "date_posted": "18, Sep, 2026",
    },
    {
        "id": 5,
        "author": "Michael",
        "title": "Building REST APIs",
        "content": "REST APIs provide a simple and reliable way for applications to communicate",
        "date_posted": "15, Sep, 2026",
    },
    {
        "id": 6,
        "author": "David",
        "title": "Understanding Pydantic",
        "content": "Pydantic makes data validation and serialization much easier in Python applications",
        "date_posted": "12, Sep, 2026",
    },
    {
        "id": 7,
        "author": "Emily",
        "title": "Python Type Hints",
        "content": "Type hints make Python code easier to understand, maintain, and debug",
        "date_posted": "10, Sep, 2026",
    },
    {
        "id": 8,
        "author": "Robert",
        "title": "Async Programming in Python",
        "content": "Asynchronous programming can help applications efficiently handle many concurrent tasks",
        "date_posted": "07, Sep, 2026",
    },
    {
        "id": 9,
        "author": "Olivia",
        "title": "Working with Databases",
        "content": "Connecting FastAPI applications to databases is straightforward with the right tools",
        "date_posted": "05, Sep, 2026",
    },
    {
        "id": 10,
        "author": "Daniel",
        "title": "API Authentication",
        "content": "Authentication is an important part of building secure and reliable APIs",
        "date_posted": "02, Sep, 2026",
    },
    {
        "id": 11,
        "author": "Sophia",
        "title": "Learning SQL",
        "content": "Understanding SQL is an essential skill for backend developers working with databases",
        "date_posted": "30, Aug, 2026",
    },
    {
        "id": 12,
        "author": "James",
        "title": "Dependency Injection in FastAPI",
        "content": "FastAPI provides a powerful dependency injection system for organizing application logic",
        "date_posted": "27, Aug, 2026",
    },
    {
        "id": 13,
        "author": "Emma",
        "title": "Testing FastAPI Applications",
        "content": "Writing automated tests helps ensure that your API behaves correctly as the project grows",
        "date_posted": "25, Aug, 2026",
    },
    {
        "id": 14,
        "author": "William",
        "title": "Building Scalable APIs",
        "content": "Good architecture and clean code are important when building APIs that need to scale",
        "date_posted": "22, Aug, 2026",
    },
    {
        "id": 15,
        "author": "Ava",
        "title": "Using HTTP Status Codes",
        "content": "Choosing the correct HTTP status code makes APIs easier for clients to understand",
        "date_posted": "19, Aug, 2026",
    },
    {
        "id": 16,
        "author": "Henry",
        "title": "FastAPI Project Structure",
        "content": "A clean project structure makes a FastAPI application easier to maintain and extend",
        "date_posted": "16, Aug, 2026",
    },
    {
        "id": 17,
        "author": "Mia",
        "title": "Handling Errors in FastAPI",
        "content": "Proper error handling provides better feedback to API clients and improves user experience",
        "date_posted": "13, Aug, 2026",
    },
    {
        "id": 18,
        "author": "Lucas",
        "title": "Using JWT Authentication",
        "content": "JWT tokens are commonly used to implement stateless authentication for web APIs",
        "date_posted": "10, Aug, 2026",
    },
    {
        "id": 19,
        "author": "Charlotte",
        "title": "API Documentation with Swagger",
        "content": "FastAPI automatically generates interactive API documentation using OpenAPI",
        "date_posted": "07, Aug, 2026",
    },
    {
        "id": 20,
        "author": "Noah",
        "title": "Deploying FastAPI",
        "content": "FastAPI applications can be deployed using servers such as Uvicorn and Gunicorn",
        "date_posted": "04, Aug, 2026",
    },
]


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html.j2", context={"posts": posts, "title": "Home Page"}
    )


@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return templates.TemplateResponse(
                request,
                "post.html.j2",
                context={"post": post, "title": post["title"][:30]},
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")


# @app.get("/output.css", include_in_schema=False)
# def get_stylesheet():
#     return FileResponse("src/output.css", media_type="text/css")


@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occured. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code, content={"detail": message}
        )

    return templates.TemplateResponse(
        request,
        "error.html.j2",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code,
    )


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"details": exception.errors()},
        )

    return templates.TemplateResponse(
        request,
        "error.html.j2",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid Request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )
