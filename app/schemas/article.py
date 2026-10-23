from datetime import datetime 
from pydantic import BaseModel, ConfigDict

class ArticleBase(BaseModel):
    titre: str
    contenu : str
    publie: bool = False

class ArticleCreate(ArticleBase):
    model_config = ConfigDict(from_attributes=True)

class ArticleUpdate(ArticleBase):
    titre: str | None = None
    contenu : str | None = None
    publie: bool | None = None

class ArticlePublic(ArticleBase):
    id : int
    created_at : datetime