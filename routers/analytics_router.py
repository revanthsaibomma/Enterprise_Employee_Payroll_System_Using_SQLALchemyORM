"""
==========================================================
File        : analytics_router.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Analytics Router Module
==========================================================
"""

from fastapi import APIRouter
from fastapi.responses import FileResponse
from visualization.charts import (
    department_chart,
    attendance_chart,
    leave_chart,
    project_chart,
    salary_distribution_chart,
    top_paid_chart
)

from services.analytics_api_service import (
    dashboard_summary_api,
    employee_summary_api,
    department_summary_api,
    payroll_summary_api,
    attendance_summary_api,
    leave_summary_api,
    project_summary_api,
    top_paid_employees_api,
    salary_distribution_api,
    dashboard_charts_api,
    run_etl_pipeline_api,
    etl_status_api
)

from schemas.analytics_schema import (
    DashboardSchema,
    EmployeeSummarySchema,
    DepartmentSummarySchema,
    PayrollSummarySchema,
    AttendanceSummarySchema,
    LeaveSummarySchema,
    ProjectSummarySchema,
    TopEmployeeSchema,
    SalaryDistributionSchema,
    ChartSchema
)



router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# -------------------------------------------------------
# Dashboard
# -------------------------------------------------------

@router.get(
    "/dashboard",
    response_model=DashboardSchema
)
def dashboard():

    return dashboard_summary_api()


# -------------------------------------------------------
# Employee Analytics
# -------------------------------------------------------

@router.get(
    "/employees",
    response_model=EmployeeSummarySchema
)
def employee_summary():

    return employee_summary_api()


# -------------------------------------------------------
# Department Analytics
# -------------------------------------------------------

@router.get(
    "/departments",
    response_model=list[DepartmentSummarySchema]
)
def department_summary():

    return department_summary_api()


# -------------------------------------------------------
# Payroll Analytics
# -------------------------------------------------------

@router.get(
    "/payroll",
    response_model=PayrollSummarySchema
)
def payroll_summary():

    return payroll_summary_api()


# -------------------------------------------------------
# Attendance Analytics
# -------------------------------------------------------

@router.get(
    "/attendance",
    response_model=AttendanceSummarySchema
)
def attendance_summary():

    return attendance_summary_api()


# -------------------------------------------------------
# Leave Analytics
# -------------------------------------------------------

@router.get(
    "/leaves",
    response_model=LeaveSummarySchema
)
def leave_summary():

    return leave_summary_api()


# -------------------------------------------------------
# Project Analytics
# -------------------------------------------------------

@router.get(
    "/projects",
    response_model=ProjectSummarySchema
)
def project_summary():

    return project_summary_api()


# -------------------------------------------------------
# Top Paid Employees
# -------------------------------------------------------

@router.get(
    "/top-paid",
    response_model=list[TopEmployeeSchema]
)
def top_paid_employees():

    return top_paid_employees_api()


# -------------------------------------------------------
# Salary Distribution
# -------------------------------------------------------

@router.get(
    "/salary-distribution",
    response_model=list[SalaryDistributionSchema]
)
def salary_distribution():

    return salary_distribution_api()

# -------------------------------------------------------
# Department Chart (Matplotlib)
# -------------------------------------------------------

@router.get("/charts/department")
def get_department_chart():

    analytics = dashboard_charts_api()

    department_data = analytics["department_chart"]

    result = department_chart(department_data)

    return FileResponse(
        path=result["chart_path"],
        media_type="image/png",
        filename="department_chart.png"
    )

@router.get("/charts/attendance")
def attendance_chart_api():

    data = dashboard_charts_api()

    result = attendance_chart(
        data["attendance_chart"]
    )

    return FileResponse(
        result["chart_path"],
        media_type="image/png"
    )

@router.get("/charts/leave")
def leave_chart_api():

    data = dashboard_charts_api()

    result = leave_chart(
        data["leave_chart"]
    )

    return FileResponse(
        result["chart_path"],
        media_type="image/png"
    )

@router.get("/charts/project")
def project_chart_api():

    data = dashboard_charts_api()

    result = project_chart(
        data["project_chart"]
    )

    return FileResponse(
        result["chart_path"],
        media_type="image/png"
    )

@router.get("/charts/salary")
def salary_chart_api():

    data = salary_distribution_api()

    result = salary_distribution_chart(data)

    return FileResponse(
        result["chart_path"],
        media_type="image/png"
    )

@router.get("/charts/top-paid")
def top_paid_chart_api():

    data = top_paid_employees_api()

    result = top_paid_chart(data)

    return FileResponse(
        result["chart_path"],
        media_type="image/png"
    )

# -------------------------------------------------------
# ETL Pipeline
# -------------------------------------------------------

@router.post(
    "/run-etl"
)
def run_etl():

    return run_etl_pipeline_api()


# -------------------------------------------------------
# ETL Status
# -------------------------------------------------------

@router.get(
    "/etl-status"
)
def etl_status():

    return etl_status_api()