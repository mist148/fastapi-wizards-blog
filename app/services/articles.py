from fastapi import HTTPException


from app import db
from app.models.article import Article

def get_article_or_404(db: db.DbSession, id: str):
    article = db.get (Article, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article Introuvable")
    return article