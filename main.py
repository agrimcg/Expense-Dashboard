from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
import models
import schemas
from database import engine, SessionLocal, Base

# ---------- DB INIT ----------
Base.metadata.create_all(bind=engine)

# ---------- APP INIT ----------
app = FastAPI(title="Expense Tracker POC")

# ---------- CORS (MANDATORY FOR FRONTEND) ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # for POC
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- DB DEPENDENCY ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==================================================
# USERS
# ==================================================

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    u = models.User(**user.dict())
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

@app.get("/users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# ==================================================
# CATEGORIES
# ==================================================

@app.post("/categories", response_model=schemas.Category)
def create_category(cat: schemas.CategoryCreate, db: Session = Depends(get_db)):
    c = models.Category(**cat.dict())
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

@app.get("/categories", response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()

# ==================================================
# EXPENSES
# ==================================================

@app.post("/expenses")
def add_expense(exp: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    user = db.get(models.User, exp.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    category = db.get(models.Category, exp.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    e = models.Expense(**exp.dict())
    db.add(e)
    db.commit()
    return {"message": "Expense added successfully"}

@app.get("/expenses")
def get_expenses(user_id: int, db: Session = Depends(get_db)):
    """
    Returns expenses with CATEGORY NAME (frontend needs this)
    """
    return db.query(
        models.Expense.id.label("id"),
        models.Expense.amount.label("amount"),
        models.Expense.expense_date.label("expense_date"),
        models.Category.name.label("category")
    ).join(models.Category).filter(
        models.Expense.user_id == user_id
    ).all()

# ==================================================
# MONTHLY SUMMARY
# ==================================================

@app.get("/expenses/summary/monthly")
def monthly_summary(
    user_id: int,
    year: int,
    month: int,
    db: Session = Depends(get_db)
):
    start = date(year, month, 1)
    end = date(year + (month == 12), (month % 12) + 1, 1)

    total = db.query(func.coalesce(func.sum(models.Expense.amount), 0)).filter(
        models.Expense.user_id == user_id,
        models.Expense.expense_date >= start,
        models.Expense.expense_date < end
    ).scalar()

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
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

