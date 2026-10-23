from datetime import datetime
from app.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, func, Boolean, false

class Article(Base):
    __tablename__ = "article"
    id: Mapped[int] = mapped_column(primary_key=True)
    titre: Mapped[str] = mapped_column(String(255))
    contenu: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    publie: Mapped[bool] = mapped_column(Boolean, default=False, server_default=false())