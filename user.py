from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import *
from app.schemas import *
from app.database import SessionLocal
from app.auth import get_role, check_role
from app.models import User
from app.schemas import UserCreate
from fastapi import HTTPException

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users", tags=["User Management"], summary="Create user")
def create_user(user:UserCreate, db: Session = Depends(get_db), role: str = Depends(get_role)):
    check_role(role, ["admin"])

    new_user =User(name=user.name, role=user.role)
    db.add(new_user)
    db.commit()
    return {"status": "success", "data": user}


@router.get("/users", tags=["User Management"], summary="Get users")
def get_users(db: Session = Depends(get_db), role: str = Depends(get_role)):
    check_role(role, ["admin"])
    return db.query(User).all()

@router.get("/")
def root():
    return {"message": "Welcome to the Financial Dashboard API!"}

def check_admin(user_role):
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")