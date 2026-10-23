from datetime import UTC, datetime, timedelta, timezone
from app.config import settings
from fastapi import HTTPException
import jwt
from pwdlib import PasswordHash
from pydantic import EmailStr
from sqlalchemy import select
from app.db import DbSession
from app.models import User
from app.schemas.user import UserCreate

password_hash = PasswordHash.recommended()

def email_conflict_409(db: DbSession, data: UserCreate):
    if db.scalar(select(User).where(User.email == data.email)):
        raise HTTPException(status_code=409, detail="email déja utilisé")
    data.hashed_password = password_hash.hash(data.hashed_password)
    user = User(**data.model_dump())
    db.add(user)
    db.commit()
    return user

def verify_email_password(db: DbSession, email: EmailStr, password: str):
    user = db.scalar(select(User).where(User.email == email))
    if user and password_hash.verify(password, user.hashed_password):
        print("oui")
        return user

def create_access_token(user: User) -> str:
    exp = datetime.now(UTC) + timedelta(minutes=30)
    return jwt.encode({"sub": str(user.id), "exp":exp}, settings.secret_key )

 