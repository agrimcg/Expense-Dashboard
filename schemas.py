from pydantic import BaseModel, Field, EmailStr, validator
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: EmailStr   # email validation

class CategoryCreate(BaseModel):
    name: str

class ExpenseCreate(BaseModel):
    user_id: int
    category_id: int
    amount: float = Field(gt=0, description="Amount must be greater than 0")
    description: str
    expense_date: date

    @validator("expense_date")
    def validate_expense_date(cls, v):
        if v > date.today():
            raise ValueError("Expense date cannot be in the future")
        return 