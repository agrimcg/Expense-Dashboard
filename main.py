from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

import models, schemas
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker POC")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    u = models.User(**user.dict())
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

@app.post("/categories")
def create_category(cat: schemas.CategoryCreate, db: Session = Depends(get_db)):
    c = models.Category(**cat.dict())
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

@app.post("/expenses")
def add_expense(exp: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    if not db.query(models.User).get(exp.user_id):
        raise HTTPException(404, "User not found")
    if not db.query(models.Category).get(exp.category_id):
        raise HTTPException(404, "Category not found")

    e = models.Expense(**exp.dict())
    db.add(e)
    db.commit()
    return {"message": "Expense added"}

@app.get("/expenses/summary/monthly")
def monthly_summary(user_id: int, year: int, month: int, db: Session = Depends(get_db)):
    start = date(year, month, 1)
    end = date(year + (month == 12), (month % 12) + 1, 1)

    total = db.query(func.sum(models.Expense.amount)).filter(
        models.Expense.user_id == user_id,
        models.Expense.expense_date >= start,
        models.Expense.expense_date < end
    ).scalar() or 0

    categories = db.query(
        models.Category.name,
        func.sum(models.Expense.amount)
    ).join(models.Expense).filter(
        models.Expense.user_id == user_id,
        models.Expense.expense_date >= start,
        models.Expense.expense_date < end
    ).group_by(models.Category.name).all()

    return {
        "total_amount": total,
        "category_summary": [
            {"category": c, "total": a} for c, a in categories
        ]
    }