from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.db import DbSession
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticlePublic, ArticleUpdate
from sqlalchemy import select


router = APIRouter(prefix="/api/articles", tags=["articles"])

@router.get("", name="articles")
def getArticles(db: DbSession) -> list[ArticlePublic]:
    return db.scalars(select(Article).order_by(Article.created_at.desc())).all()

@router.get("/{id}",name="id", responses={404: {"description": "Article Introuvable"}})
def getArticleById(db: DbSession, id: int) -> ArticlePublic:
    article = db.get(Article, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article Introuvable")
    return article

@router.post("", name="create_article", response_model=ArticlePublic, status_code=201)
def create(data: ArticleCreate, db: DbSession) -> ArticlePublic:
    article = Article(**data.model_dump())
    db.add(article)
    db.commit()
    return article

@router.patch("/{id}", name="update_article")
def update(data: ArticleUpdate, id: int, db: DbSession) -> ArticlePublic:
    article = db.get(Article, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article Introuvable")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(article, key, value)
    db.commit()
    return article

@router.delete("/{id}", name="delete_article", status_code=204)
def delete(db: DbSession, id: int):
    article = db.get (Article, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article Introuvable")
    db.delete(article)
    db.commit()
