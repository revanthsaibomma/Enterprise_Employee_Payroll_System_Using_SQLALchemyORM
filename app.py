from fastapi import FastAPI

import models
from database import Base, engine

from models.employee_model import Employee
from models.department_model import Department
from models.role_model import Role
from models.attendance_model import Attendance
from models.leave_model import LeaveRequest
from models.payroll_model import Payroll
from models.project_model import Project
from models.employee_project_model import EmployeeProject
from models.task_model import Task
from models.salary_model import Salary
from models.analytics_model import AnalyticsSummary

from routers.employee_router import router as employee_router
from routers.department_router import router as department_router
from routers.attendance_router import router as attendance_router
from routers.leave_router import router as leave_router
from routers.project_router import router as project_router
from routers.payroll_router import router as payroll_router
from routers.report_router import router as report_router
from routers.analytics_router import router as analytics_router

import sys
print(sys.executable)

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Enterprise Employee Payroll Management System",
    version="1.0.0",
    description="Employee Payroll Management REST API"
)

app.include_router(employee_router)
app.include_router(department_router)
app.include_router(attendance_router)
app.include_router(leave_router)
app.include_router(project_router)
app.include_router(payroll_router)
app.include_router(report_router)
app.include_router(analytics_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise Employee Payroll Management API"
    }