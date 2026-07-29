# Enterprise Employee Payroll Management System

An Enterprise Employee Payroll Management System developed using **FastAPI**, **Python**, **SQLAlchemy**, **MySQL**, and **Matplotlib**. The application provides employee management, attendance tracking, leave management, payroll processing, analytics dashboards, and RESTful APIs for enterprise organizations.

---

# Developer

**Revanth Sai Bomma**

---

# Features

## Employee Management
- Add Employee
- Update Employee
- Delete Employee
- View Employee Details
- Search Employee
- Employee Profile Management

## Department Management
- Add Department
- Update Department
- Delete Department
- Department-wise Employee Count

## Attendance Management
- Daily Attendance
- Attendance Reports
- Attendance Summary

## Leave Management
- Apply Leave
- Leave Approval/Rejection
- Leave History
- Leave Reports

## Payroll Management
- Salary Calculation
- Bonus Calculation
- Deduction Calculation
- Net Salary Calculation
- Payroll History
- Payroll Reports

## Analytics Dashboard
- Department-wise Employee Count
- Attendance Analysis
- Leave Analysis
- Salary Distribution
- Top Paid Employees
- Project Status Dashboard

---

# Technology Stack

## Backend
- Python
- FastAPI

## Database
- MySQL
- SQLAlchemy ORM

## Data Validation
- Pydantic

## Visualization
- Matplotlib

## API Testing
- Swagger UI
- Postman

---

# Project Structure

```
Enterprise-Employee-Payroll-System/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   ├── database.py
│   ├── settings.py
│   └── __init__.py
│
├── models/
│   ├── employee.py
│   ├── department.py
│   ├── attendance.py
│   ├── leave.py
│   ├── payroll.py
│   ├── project.py
│   └── __init__.py
│
├── schemas/
│   ├── employee_schema.py
│   ├── department_schema.py
│   ├── attendance_schema.py
│   ├── leave_schema.py
│   ├── payroll_schema.py
│   ├── project_schema.py
│   └── __init__.py
│
├── repository/
│   ├── employee_repository.py
│   ├── department_repository.py
│   ├── attendance_repository.py
│   ├── leave_repository.py
│   ├── payroll_repository.py
│   ├── analytics_repository.py
│   └── __init__.py
│
├── services/
│   ├── employee_service.py
│   ├── department_service.py
│   ├── attendance_service.py
│   ├── leave_service.py
│   ├── payroll_service.py
│   ├── analytics_api_service.py
│   └── __init__.py
│
├── routers/
│   ├── employee_router.py
│   ├── department_router.py
│   ├── attendance_router.py
│   ├── leave_router.py
│   ├── payroll_router.py
│   ├── analytics_router.py
│   └── __init__.py
│
├── visualization/
│   ├── charts.py
│   ├── dashboard.py
│   └── __init__.py
│
├── charts/
│   ├── department_chart.png
│   ├── attendance_chart.png
│   ├── leave_chart.png
│   ├── project_chart.png
│   ├── salary_distribution.png
│   └── top_paid_chart.png
│
├── utils/
│   ├── helpers.py
│   ├── validators.py
│   └── __init__.py
│
├── static/
│
├── templates/
│
└── tests/
    ├── test_employee.py
    ├── test_department.py
    ├── test_attendance.py
    ├── test_leave.py
    ├── test_payroll.py
    └── test_analytics.py
```

---

# REST API Modules

- Employee Management APIs
- Department Management APIs
- Attendance Management APIs
- Leave Management APIs
- Payroll Management APIs
- Analytics Dashboard APIs

---

# Analytics Charts

The application generates the following analytics using Matplotlib:

- 📊 Department Employee Count (Bar Chart)
- 📈 Attendance Analysis (Line Chart)
- 🍩 Leave Status (Donut Chart)
- 📊 Salary Distribution (Horizontal Bar Chart)
- 📊 Top Paid Employees (Horizontal Bar Chart)
- 📊 Project Status (Horizontal Bar Chart)

---

# API Endpoints

## Employee

- GET /employees
- GET /employees/{id}
- POST /employees
- PUT /employees/{id}
- DELETE /employees/{id}

## Department

- GET /departments
- POST /departments
- PUT /departments/{id}
- DELETE /departments/{id}

## Attendance

- GET /attendance
- POST /attendance

## Leave

- GET /leave
- POST /leave

## Payroll

- GET /payroll
- POST /payroll

## Analytics

- GET /analytics/charts/department
- GET /analytics/charts/attendance
- GET /analytics/charts/leave
- GET /analytics/charts/project
- GET /analytics/charts/salary
- GET /analytics/charts/top-paid

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Enterprise-Employee-Payroll-System.git
```

## Navigate to Project

```bash
cd Enterprise-Employee-Payroll-System
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn main:app --reload
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Future Enhancements

- JWT Authentication
- Role-Based Access Control (RBAC)
- Email Notifications
- Payroll PDF Generation
- Employee Self-Service Portal
- Dashboard Export (PDF/Excel)
- Performance Evaluation Module
- Cloud Deployment
- Docker Support
- CI/CD Pipeline Integration

---

# Testing

The project includes testing for:

- Employee Module
- Department Module
- Attendance Module
- Leave Module
- Payroll Module
- Analytics Module

---

# Author

**Revanth Sai Bomma**

---

# License

This project is developed for academic and educational purposes.