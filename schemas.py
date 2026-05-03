from pydantic import BaseModel
from datetime import date

# =========================
# USERS
# =========================

class UserCreate(BaseModel):
    name: str
    email: str


class User(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# =========================
# CATEGORIES
# =========================

class CategoryCreate(BaseModel):
    name: str


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# =========================
# EXPENSES
# =========================

class ExpenseCreate(BaseModel):
    user_id: int
    category_id: int
    amount: float
    expense_date: date
