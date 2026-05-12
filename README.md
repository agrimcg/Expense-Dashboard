Expense Dashboard – Proof of Concept (POC)
A full‑stack Expense Dashboard Proof of Concept (POC) built using FastAPI (Python) for the backend and HTML, CSS, and Vanilla JavaScript for the frontend.
This application demonstrates complete CRUD functionality for Users, Categories, and Expenses, along with a Monthly Expense Summary view. The project focuses on clean architecture, practical implementation, and professional Git/GitHub practices.

#Overview
The Expense Dashboard POC allows users to:

Manage multiple users
Create and manage expense categories,
Track daily expenses per user,
View monthly expense summaries with category‑wise breakdown,
Maintain structured backend APIs with a simple frontend dashboard.

The goal of this project is to showcase end‑to‑end full‑stack development using FastAPI and Vanilla JavaScript.

#Features
1.User Management
Create users,
Edit users,
Delete users,
Select an active user.

2.Category Management
Create categories,
Edit categories,
Delete categories,
Restrict deletion of categories that are in use.

3.Expense Management
Add expenses for an active user,
Edit expenses,
Delete expenses,
Validate expense amount, date, and category.

4.Monthly Summary
Select month and year,
View total monthly expenses,
View category‑wise expense totals.

5.UI & UX
Single‑page dashboard,
Multiple views (Add Expense, Expenses, Summary, Users, Categories),
Dark theme user interface,
Toast notifications for actions,
Responsive layout.


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
├── main.py
├── models.py
├── schemas.py
├── database.py
├── index.html
├── expense_tracker.db
├── requirements.txt
├── pytest.ini
├── .gitignore
├── tests/
│   ├── conftest.py
│   └── test_api.py
└── README.md

#Backend Setup
Create Virtual Environment :
python -m venv venv

Activate Virtual Environment : 
Windows
venv\Scripts\activate

Install Dependencies : 
pip install -r requirements.txt

Run Backend Server (serves the API and the dashboard at `/`):

uvicorn main:app --reload

Application and API base URL:
http://127.0.0.1:8000

Swagger API documentation:
http://127.0.0.1:8000/docs

Open the dashboard in the browser at `http://127.0.0.1:8000/` (same origin as the API). Opening `index.html` directly as a `file://` page will block API calls in most browsers.

#Tests
API integration tests use `pytest` and an isolated in-memory SQLite database (`EXPENSE_DB_URL` is set in `tests/conftest.py`; the app uses `StaticPool` so in-memory SQLite works across threads).

Run:

pytest

In the app, open **Reports** and use **Scope**: **All users (combined)**, **Active profile (header)**, or **Only: &lt;name&gt;** for any profile. The category table, monthly bar chart, and multi-year line chart all follow that scope; with a single profile selected, the second chart switches to **categories for that profile** for the chart year. The “by profile” comparison chart appears only when scope is **All users**.

API Endpoints
Users
POST    /users
GET     /users
GET     /users/{user_id}
PUT     /users/{user_id}
DELETE  /users/{user_id}

Categories
POST    /categories
GET     /categories
GET     /categories/{category_id}
PUT     /categories/{category_id}
DELETE  /categories/{category_id}

Expenses
POST    /expenses
GET     /expenses?user_id={id}
GET     /expenses/{expense_id}
PUT     /expenses/{expense_id}   (optional: user_id to move expense to another profile)
DELETE  /expenses/{expense_id}

Monthly summary (category breakdown for one calendar month)
GET /expenses/summary/monthly?year=&month=
    Optional: user_id — omit to aggregate across all profiles.

Reports (for dashboards & charts)
GET /reports/summary/year?year=&user_id=
    Full-year total, category breakdown, and per-month totals (12 points). Omit user_id for all users.

GET /reports/timeseries/years?from_year=&to_year=&user_id=
    One total per calendar year in the inclusive range. Omit user_id for all users.

GET /reports/by-user?year=&month=
    Spend per profile: month omitted = entire year; month=1–12 = that month only. Always lists every user (0 if no spend).


#Data Models
User
{
  "id": 1,
  "name": "User Name",
  "email": "user@example.com",
  "phone": ""
}

Category
{
  "id": 1,
  "name": "Food",
  "description": ""
}

Expense
{
  "id": 101,
  "user_id": 1,
  "category_id": 2,
  "name": "Lunch",
  "amount": 250,
  "expense_date": "2024-04-15",
  "notes": "",
  "payment_method": ""
}

#Validations & Rules

Expense amount must be greater than zero
Expense date is mandatory
Categories in use cannot be deleted
Confirmation is required before delete actions


#Limitations (POC Scope)

No authentication or authorization
No role‑based access control
API tests via `pytest` (see Tests above)
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

