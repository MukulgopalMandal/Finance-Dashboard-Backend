from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal
from app.auth import get_role, check_role
from app.models import Record
from app.schemas import RecordCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/records", tags=["Financial Records"], summary="Create record")
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db), role: str = Depends(get_role)):
    check_role(role, ["admin"])

    rec = models.Record(**record.dict())
    db.add(rec)
    db.commit()
    return {"status": "created"}


@router.get("/records", tags=["Financial Records"], summary="Get records with filters")
def get_records(
    category: str = None,
    type: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    role: str = Depends(get_role)
):
    check_role(role, ["admin", "analyst", "viewer"])

    query = db.query(models.Record).filter(models.Record.is_deleted == 0)

    if category:
        query = query.filter(models.Record.category == category)
    if type:
        query = query.filter(models.Record.type == type)

    return query.offset(skip).limit(limit).all()


@router.delete("/records/{id}", tags=["Financial Records"], summary="Soft delete record")
def delete_record(id: int, db: Session = Depends(get_db), role: str = Depends(get_role)):
    check_role(role, ["admin"])

    rec = db.query(models.Record).filter(models.Record.id == id).first()

    if not rec:
        raise HTTPException(status_code=404, detail="Record not found")

    rec.is_deleted = 1
    db.commit()
    return {"status": "deleted"}

from fastapi import APIRouter, HTTPException

router = APIRouter()

# role check function
def check_admin(user_role):
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

# create record (ONLY ADMIN)
@router.post("/records")
def create_record(role: str):
    check_admin(role)   # 🔥 this enforces access control
    
    return {"message": "Record created successfully"}