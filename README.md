Expense Dashboard – Proof of Concept (POC)
A full‑stack Expense Dashboard Proof of Concept (POC) built using FastAPI (Python) for the backend and HTML, CSS, and Vanilla JavaScript for the frontend.
This application demonstrates complete CRUD functionality for Users, Categories, and Expenses, along with a Monthly Expense Summary view. The project focuses on clean architecture, practical implementation, and professional Git/GitHub practices.

#Overview
The Expense Dashboard POC allows users to:

Manage multiple users
Create and manage expense categories
Track daily expenses per user
View monthly expense summaries with category‑wise breakdown
Maintain structured backend APIs with a simple frontend dashboard

The goal of this project is to showcase end‑to‑end full‑stack development using FastAPI and Vanilla JavaScript.

#Features
1.User Management
Create users
Edit users
Delete users
Select an active user

2.Category Management
Create categories
Edit categories
Delete categories
Restrict deletion of categories that are in use

3.Expense Management
Add expenses for an active user
Edit expenses
Delete expenses
Validate expense amount, date, and category

4.Monthly Summary
Select month and year
View total monthly expenses
View category‑wise expense totals

5.UI & UX
Single‑page dashboard
Multiple views (Add Expense, Expenses, Summary, Users, Categories)
Dark theme user interface
Toast notifications for actions
Responsive layout


#Tech Stack
Backend

.Python 3.x
.FastAPI
.SQLAlchemy
.SQLite
.Uvicorn

Frontend

.HTML5
.CSS3

#Project structure
Expense-Dashboard/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
└── README.md

#Backend Setup
Create Virtual Environment
python -m venv venv

Activate Virtual Environment
Windows
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run Backend Server
cd backend
uvicorn main:app --reload

Backend will be available at:
http://127.0.0.1:8000

Swagger API documentation:
http://127.0.0.1:8000/docs


#Frontend Setup

Navigate to the frontend directory
Open index.html in a browser (Chrome or Edge recommended)

No frontend server or build setup is required for this POC.

API Endpoints
Users
POST    /users
GET     /users
DELETE  /users/{user_id}

Categories
POST    /categories
GET     /categories
DELETE  /categories/{category_id}

Expenses
POST    /expenses
GET     /expenses?user_id={id}
DELETE  /expenses/{expense_id}

Monthly Summary
GET /expenses/summary/monthly?user_id=&year=&month=


#Data Models
User
{
  "id": 1,
  "name": "User Name",
  "email": "user@example.com"
}

Category
{
  "id": 1,
  "name": "Food"
}

Expense
{
  "id": 101,
  "userId": 1,
  "name": "Lunch",
  "category": "Food",
  "amount": 250,
  "date": "2024-04-15"
}

#Validations & Rules

An active user must be selected before adding expenses
Expense amount must be greater than zero
Expense date is mandatory
Categories in use cannot be deleted
Confirmation is required before delete actions


#Limitations (POC Scope)

No authentication or authorization
No role‑based access control
No automated test coverage
Not production‑hardened


#Future Enhancements

User authentication using JWT
Backend‑driven frontend state
Charts and analytics
Export reports (CSV / PDF)
React or Angular frontend
Dockerized deployment
Unit and integration tests


Author
Expense Dashboard – Proof of Concept
Developed as a full‑stack POC using FastAPI and Vanilla JavaScript, focusing on clean design, maintainable code, and professional GitHub practices.

Vanilla JavaScript

