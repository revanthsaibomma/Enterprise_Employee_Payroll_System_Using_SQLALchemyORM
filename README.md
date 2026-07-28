# Enterprise Employee Payroll Management System

A RESTful Employee Payroll Management System developed using **Python**, **FastAPI**, **SQLAlchemy ORM**, and **MySQL**. The application manages employees, departments, attendance, leave, projects, payroll, and reports through a Swagger-documented REST API.

---

## Features

- Employee Management
- Department Management
- Attendance Management
- Leave Management
- Project Management
- Payroll Management
- Dashboard Reports
- REST API using FastAPI
- Interactive Swagger Documentation
- SQLAlchemy ORM
- MySQL Database
- Input Validation
- Custom Exception Handling
- Logging Support

---

## Technology Stack

- Python 3.x
- FastAPI
- SQLAlchemy ORM
- MySQL
- Pydantic
- Uvicorn
- PyMySQL

---

## Project Structure

```
Enterprise_Employee_Payroll_System
│
├── app.py
├── database.py
├── database_initializer.py
│
├── models/
│   ├── employee_model.py
│   ├── department_model.py
│   ├── attendance_model.py
│   ├── leave_model.py
│   ├── project_model.py
│   ├── payroll_model.py
│   ├── salary_model.py
│   ├── task_model.py
│   └── role_model.py
│
├── routers/
│   ├── employee_router.py
│   ├── department_router.py
│   ├── attendance_router.py
│   ├── leave_router.py
│   ├── project_router.py
│   ├── payroll_router.py
│   └── report_router.py
│
├── services/
│   ├── employee_api_service.py
│   ├── department_api_service.py
│   ├── attendance_api_service.py
│   ├── leave_api_service.py
│   ├── project_api_service.py
│   ├── payroll_api_service.py
│   └── report_api_service.py
│
├── schemas/
│   ├── employee_schema.py
│   ├── department_schema.py
│   ├── attendance_schema.py
│   ├── leave_schema.py
│   ├── project_schema.py
│   └── payroll_schema.py
│
├── validations/
├── exceptions/
├── utilities/
└── README.md
```

---

## Modules

### Employee
- Add Employee
- Search Employee
- Update Employee
- Delete Employee
- Display All Employees

### Department
- Add Department
- Search Department
- Update Department
- Delete Department
- Display All Departments

### Attendance
- Mark Attendance
- Search Attendance
- Update Attendance
- Delete Attendance
- Display All Attendance Records

### Leave
- Apply Leave
- Search Leave
- Update Leave Status
- Delete Leave
- Display All Leave Records

### Project
- Add Project
- Search Project
- Update Project
- Delete Project
- Display All Projects

### Payroll
- Generate Payroll
- Search Payroll
- Update Payroll
- Delete Payroll
- Display All Payroll Records

### Reports
- Employee Report
- Department Report
- Project Report
- Payroll Report
- Dashboard Report

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Enterprise_Employee_Payroll_System.git
```

Move into the project directory:

```bash
cd Enterprise_Employee_Payroll_System
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic email-validator
```

---

## Configure Database

Update the MySQL connection details in `database.py`.

Example:

```python
DATABASE_URL = "mysql+pymysql://root:password@localhost/payroll_db"
```

Replace:

- root
- password
- payroll_db

with your database credentials.

---

## Run the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Employee

| Method | Endpoint |
|---------|----------|
| POST | `/employees/` |
| GET | `/employees/` |
| GET | `/employees/{employee_id}` |
| PUT | `/employees/{employee_id}` |
| DELETE | `/employees/{employee_id}` |

### Department

| Method | Endpoint |
|---------|----------|
| POST | `/departments/` |
| GET | `/departments/` |
| GET | `/departments/{department_id}` |
| PUT | `/departments/{department_id}` |
| DELETE | `/departments/{department_id}` |

### Attendance

| Method | Endpoint |
|---------|----------|
| POST | `/attendance/` |
| GET | `/attendance/` |
| GET | `/attendance/{employee_id}` |
| PUT | `/attendance/{attendance_id}` |
| DELETE | `/attendance/{attendance_id}` |

### Leave

| Method | Endpoint |
|---------|----------|
| POST | `/leaves/` |
| GET | `/leaves/` |
| GET | `/leaves/{employee_id}` |
| PUT | `/leaves/{leave_id}` |
| DELETE | `/leaves/{leave_id}` |

### Project

| Method | Endpoint |
|---------|----------|
| POST | `/projects/` |
| GET | `/projects/` |
| GET | `/projects/{project_id}` |
| PUT | `/projects/{project_id}` |
| DELETE | `/projects/{project_id}` |

### Payroll

| Method | Endpoint |
|---------|----------|
| POST | `/payrolls/` |
| GET | `/payrolls/` |
| GET | `/payrolls/{employee_id}` |
| PUT | `/payrolls/{payroll_id}` |
| DELETE | `/payrolls/{payroll_id}` |

### Reports

| Method | Endpoint |
|---------|----------|
| GET | `/reports/employees` |
| GET | `/reports/departments` |
| GET | `/reports/projects` |
| GET | `/reports/payrolls` |
| GET | `/reports/dashboard` |

---

## Architecture

```
Client (Browser / Postman / Swagger)
              │
              ▼
          FastAPI Router
              │
              ▼
       Pydantic Schemas
              │
              ▼
      Service Layer (Business Logic)
              │
              ▼
    SQLAlchemy ORM Models
              │
              ▼
         MySQL Database
```

---

## Key Features

- Modular Architecture
- RESTful API Design
- Input Validation
- Exception Handling
- SQLAlchemy ORM
- Swagger API Documentation
- Layered Project Structure
- Easy to Extend and Maintain

---

## Future Enhancements

- JWT Authentication
- Role-Based Access Control (RBAC)
- Email Notifications
- PDF Payroll Reports
- Excel Report Export
- Docker Deployment
- Unit Testing
- CI/CD Integration

---

## Author

**Revanth Sai Bomma**

---

## License

This project is intended for educational and learning purposes.