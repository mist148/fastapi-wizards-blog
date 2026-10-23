from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routers import articles, auth, exercices
from app.db import engine


@asynccontextmanager
async def lifespan(app:  FastAPI):
    yield
    engine.dispose()

app = FastAPI(title="Blog des Wizards", lifespan=lifespan)
app.include_router(exercices.router)
app.include_router(articles.router)
app.include_router(auth.router)
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"titre": "Le blog" ,"articles" : articles.getArticles()})

@app.get("/health")
def home() -> dict[str, str]:
    return {"status": "ok"}



