from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import defaultdict
from app import models
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


@router.get("/summary", tags=["Dashboard"], summary="Overall summary")
def summary(db: Session = Depends(get_db), role: str = Depends(get_role)):
    check_role(role, ["admin", "analyst"])

    records = db.query(models.Record).filter(models.Record.is_deleted == 0).all()

    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }


@router.get("/summary/monthly", tags=["Dashboard"], summary="Monthly trends")
def monthly_summary(db: Session = Depends(get_db), role: str = Depends(get_role)):
    check_role(role, ["admin", "analyst"])

    records = db.query(models.Record).all()
    result = defaultdict(lambda: {"income": 0, "expense": 0})

    for r in records:
        month = r.date[:7]
        result[month][r.type] += r.amount

    return result

@router.get("/dashboard")
def get_dashboard():
    return {
        "total_income": 5000,
        "total_expense": 3000,
        "balance": 2000
    }