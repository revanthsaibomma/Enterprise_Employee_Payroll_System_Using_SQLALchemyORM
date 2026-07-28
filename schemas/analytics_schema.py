"""
==========================================================
File        : analytics_schema.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Analytics Schemas
==========================================================
"""

from typing import List, Dict, Any
from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ==========================================================
# Dashboard Schema
# ==========================================================

class DashboardSchema(BaseModel):

    total_employees: int

    active_employees: int

    inactive_employees: int

    total_departments: int

    total_projects: int

    active_projects: int

    completed_projects: int

    pending_projects: int

    total_payroll: float

    average_salary: float

    highest_salary: float

    lowest_salary: float

    attendance_percentage: float

    approved_leaves: int

    pending_leaves: int

    rejected_leaves: int

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Employee Summary
# ==========================================================

class EmployeeSummarySchema(BaseModel):

    total_employees: int

    active_employees: int

    inactive_employees: int


# ==========================================================
# Department Summary
# ==========================================================

class DepartmentSummarySchema(BaseModel):

    department_name: str

    employee_count: int


# ==========================================================
# Payroll Summary
# ==========================================================

class PayrollSummarySchema(BaseModel):

    total_payroll: float

    average_salary: float

    highest_salary: float

    lowest_salary: float

    total_bonus: float

    total_deduction: float


# ==========================================================
# Attendance Summary
# ==========================================================

class AttendanceSummarySchema(BaseModel):

    present: int

    absent: int

    attendance_percentage: float


# ==========================================================
# Leave Summary
# ==========================================================

class LeaveSummarySchema(BaseModel):

    approved: int

    pending: int

    rejected: int

    total_leave_days: int


# ==========================================================
# Project Summary
# ==========================================================

class ProjectSummarySchema(BaseModel):

    total_projects: int

    active_projects: int

    completed_projects: int

    pending_projects: int

    total_budget: float

    average_budget: float


# ==========================================================
# Top Paid Employee
# ==========================================================

class TopEmployeeSchema(BaseModel):

    employee_id: int

    employee_name: str

    department_name: str

    net_salary: float


# ==========================================================
# Salary Distribution
# ==========================================================

class SalaryDistributionSchema(BaseModel):

    department_name: str

    total_salary: float


# ==========================================================
# Chart Schema
# ==========================================================

class ChartSchema(BaseModel):

    chart_name: str

    chart_data: Dict[str, Any]


# ==========================================================
# Dashboard Charts
# ==========================================================

class DashboardChartsSchema(BaseModel):

    dashboard: DashboardSchema

    charts: List[ChartSchema]


# ==========================================================
# ETL Response
# ==========================================================

class ETLResponseSchema(BaseModel):

    message: str

    status: str

    execution_time: str


# ==========================================================
# ETL Status
# ==========================================================

class ETLStatusSchema(BaseModel):

    last_run: datetime | None = None

    status: str

    total_records_processed: int

    total_records_loaded: int