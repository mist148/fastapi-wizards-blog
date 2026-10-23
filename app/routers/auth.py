from datetime import timedelta
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.db import DbSession
from app.schemas.user import Token, UserCreate, UserPublic
from app.services.user import create_access_token, email_conflict_409, verify_email_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", name="register", response_model=UserPublic, status_code=201)
def create(data: UserCreate, db: DbSession) -> UserPublic:
    return email_conflict_409(db, data)


@router.post("/token", name="token")
def authenticate_user(db: DbSession, data: UserCreate) -> Token:
    user = verify_email_password(db, data.email, data.hashed_password)
    if user:
        return Token(access_token=create_access_token(user))
    raise HTTPException(status_code=404, detail="utilisateur introuvable")

@router.get("/me", name="token")
def get_current_user():
    return