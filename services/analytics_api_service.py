"""
==========================================================
File        : analytics_api_service.py
Project     : Enterprise Employee Payroll Management System
Description : Analytics API Service (CSV + PySpark)
==========================================================
"""

from pyspark.sql.functions import (
    col,
    count,
    avg,
    sum,
    max,
    min
)

from etl.extract import Extract
from etl.transform import Transform

from utilities.logger_config import (
    application,
    exception
)

from exceptions.custom_exception import DatabaseException


# ==========================================================
# Load & Transform CSV Data
# ==========================================================

def load_data():
    """
    Load all CSV files and apply transformations.

    Returns:
        dict : Dictionary containing transformed
               PySpark DataFrames.
    """

    try:

        extractor = Extract()

        transformer = Transform()

        raw_data = extractor.extract_all()

        transformed_data = transformer.transform_all(raw_data)

        return transformed_data

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Load Analytics Data."
        )


# ==========================================================
# Dashboard Analytics
# ==========================================================

def dashboard_summary_api():

    """
    Dashboard Summary Analytics
    """

    try:

        data = load_data()
        print(data.keys())
        print("Employees:", data["employees"].count())
        print("Payroll:", data["payroll"].count())
        print("Projects:", data["projects"].count())
        print("Departments:", data["departments"].count())
        print("Attendance:", data["attendance"].count())
        print("Leave_requests:", data["leave_requests"].count())

        employees = data["employees"]
        departments = data["departments"]
        payroll = data["payroll"]
        attendance = data["attendance"]
        leave_requests = data["leave_requests"]
        projects = data["projects"]
        

        # --------------------------------------------
        # Employee Summary
        # --------------------------------------------

        total_employees = employees.count()

        active_employees = employees.filter(
            col("status") == "ACTIVE"
        ).count()

        inactive_employees = employees.filter(
            col("status") == "INACTIVE"
        ).count()

        # --------------------------------------------
        # Department Summary
        # --------------------------------------------

        total_departments = departments.count()

        # --------------------------------------------
        # Project Summary
        # --------------------------------------------

        total_projects = projects.count()

        active_projects = projects.filter(
            col("status") == "Active"
        ).count()

        completed_projects = projects.filter(
            col("status") == "Completed"
        ).count()

        pending_projects = projects.filter(
            col("status") == "Pending"
        ).count()

        # --------------------------------------------
        # Payroll Summary
        # --------------------------------------------

        payroll_summary = payroll.agg(

            sum("net_salary").alias("total_payroll"),

            avg("net_salary").alias("average_salary"),

            max("net_salary").alias("highest_salary"),

            min("net_salary").alias("lowest_salary")

        ).collect()[0]

        total_payroll = round(
            payroll_summary["total_payroll"] or 0,
            2
        )

        average_salary = round(
            payroll_summary["average_salary"] or 0,
            2
        )

        highest_salary = round(
            payroll_summary["highest_salary"] or 0,
            2
        )

        lowest_salary = round(
            payroll_summary["lowest_salary"] or 0,
            2
        )

        # --------------------------------------------
        # Leave Summary
        # --------------------------------------------

        approved_leaves = leave_requests.filter(
            col("status") == "Approved"
        ).count()

        pending_leaves = leave_requests.filter(
            col("status") == "Pending"
        ).count()

        rejected_leaves = leave_requests.filter(
            col("status") == "Rejected"
        ).count()

        # --------------------------------------------
        # Attendance Summary
        # --------------------------------------------

        total_attendance = attendance.count()

        present = attendance.filter(
            col("status") == "Present"
        ).count()

        attendance_percentage = 0.0

        if total_attendance > 0:

            attendance_percentage = round(

                (present / total_attendance) * 100,

                2

            )

        application(
            "Dashboard Analytics Generated Successfully."
        )

        return {

            "total_employees": total_employees,
            "active_employees": active_employees,
            "inactive_employees": inactive_employees,

            "total_departments": total_departments,

            "total_projects": total_projects,
            "active_projects": active_projects,
            "completed_projects": completed_projects,
            "pending_projects": pending_projects,

            "total_payroll": total_payroll,
            "average_salary": average_salary,
            "highest_salary": highest_salary,
            "lowest_salary": lowest_salary,

            "attendance_percentage": attendance_percentage,

            "approved_leaves": approved_leaves,
            "pending_leaves": pending_leaves,
            "rejected_leaves": rejected_leaves

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Dashboard Analytics."
        )


# ==========================================================
# Employee Analytics
# ==========================================================

def employee_summary_api():

    """
    Employee Summary Analytics
    """

    try:

        employees = load_data()["employees"]

        total_employees = employees.count()

        active_employees = employees.filter(
            col("status") == "ACTIVE"
        ).count()

        inactive_employees = employees.filter(
            col("status") == "INACTIVE"
        ).count()

        application(
            "Employee Analytics Generated Successfully."
        )

        return {

            "total_employees": total_employees,

            "active_employees": active_employees,

            "inactive_employees": inactive_employees

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Employee Analytics."
        )


# ==========================================================
# Department Analytics
# ==========================================================

def department_summary_api():

    """
    Department Summary Analytics
    """

    try:

        data = load_data()

        employees = data["employees"]

        departments = data["departments"]

        department_summary = (

            departments

            .join(

                employees,

                "department_id",

                "left"

            )

            .groupBy(

                "department_name"

            )

            .agg(

                count("employee_id").alias(
                    "employee_count"
                )

            )

            .orderBy(
                "department_name"
            )

        )

        application(
            "Department Analytics Generated Successfully."
        )

        return [

            {

                "department_name": row["department_name"],

                "employee_count": row["employee_count"]

            }

            for row in department_summary.collect()

        ]

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Department Analytics."
        )

# ==========================================================
# Payroll Analytics
# ==========================================================

def payroll_summary_api():

    """
    Payroll Summary Analytics
    """

    try:

        payroll = load_data()["payroll"]

        payroll_summary = payroll.agg(

            sum("net_salary").alias("total_payroll"),

            avg("net_salary").alias("average_salary"),

            max("net_salary").alias("highest_salary"),

            min("net_salary").alias("lowest_salary"),

            sum("bonus").alias("total_bonus"),

            sum("deduction").alias("total_deduction")

        ).collect()[0]

        application(
            "Payroll Analytics Generated Successfully."
        )

        return {

            "total_payroll": round(
                payroll_summary["total_payroll"] or 0,
                2
            ),

            "average_salary": round(
                payroll_summary["average_salary"] or 0,
                2
            ),

            "highest_salary": round(
                payroll_summary["highest_salary"] or 0,
                2
            ),

            "lowest_salary": round(
                payroll_summary["lowest_salary"] or 0,
                2
            ),

            "total_bonus": round(
                payroll_summary["total_bonus"] or 0,
                2
            ),

            "total_deduction": round(
                payroll_summary["total_deduction"] or 0,
                2
            )

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Payroll Analytics."
        )


# ==========================================================
# Attendance Analytics
# ==========================================================

def attendance_summary_api():

    """
    Attendance Summary Analytics
    """

    try:

        attendance = load_data()["attendance"]

        total_records = attendance.count()

        present = attendance.filter(
            col("status") == "Present"
        ).count()

        absent = attendance.filter(
            col("status") == "Absent"
        ).count()

        attendance_percentage = 0.0

        if total_records > 0:

            attendance_percentage = round(

                (present / total_records) * 100,

                2

            )

        application(
            "Attendance Analytics Generated Successfully."
        )

        return {

            "present": present,

            "absent": absent,

            "attendance_percentage": attendance_percentage

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Attendance Analytics."
        )


# ==========================================================
# Leave Analytics
# ==========================================================

def leave_summary_api():

    """
    Leave Summary Analytics
    """

    try:

        leave_requests = load_data()["leave_requests"]

        approved = leave_requests.filter(
            col("status") == "Approved"
        ).count()

        pending = leave_requests.filter(
            col("status") == "Pending"
        ).count()

        rejected = leave_requests.filter(
            col("status") == "Rejected"
        ).count()

        total_leave_days = leave_requests.agg(

            sum("leave_days").alias(
                "total_leave_days"
            )

        ).collect()[0]["total_leave_days"] or 0

        application(
            "Leave Analytics Generated Successfully."
        )

        return {

            "approved": approved,

            "pending": pending,

            "rejected": rejected,

            "total_leave_days": total_leave_days

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Leave Analytics."
        )


# ==========================================================
# Project Analytics
# ==========================================================

def project_summary_api():

    """
    Project Summary Analytics
    """

    try:

        projects = load_data()["projects"]

        total_projects = projects.count()

        active_projects = projects.filter(
            col("status") == "Active"
        ).count()

        completed_projects = projects.filter(
            col("status") == "Completed"
        ).count()

        pending_projects = projects.filter(
            col("status") == "Pending"
        ).count()

        budget_summary = projects.agg(

            sum("project_budget").alias(
                "total_budget"
            ),

            avg("project_budget").alias(
                "average_budget"
            )

        ).collect()[0]

        application(
            "Project Analytics Generated Successfully."
        )

        return {

            "total_projects": total_projects,

            "active_projects": active_projects,

            "completed_projects": completed_projects,

            "pending_projects": pending_projects,

            "total_budget": round(
                budget_summary["total_budget"] or 0,
                2
            ),

            "average_budget": round(
                budget_summary["average_budget"] or 0,
                2
            )

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Project Analytics."
        )

# ==========================================================
# Top Paid Employees Analytics
# ==========================================================

def top_paid_employees_api():

    """
    Top 10 Highest Paid Employees
    """

    try:

        data = load_data()

        employees = data["employees"]
        departments = data["departments"]
        payroll = data["payroll"]

        top_paid = (

            employees

            .join(
                payroll,
                "employee_id"
            )

            .join(
                departments,
                "department_id"
            )

            .select(
                "employee_id",
                "employee_name",
                "department_name",
                "net_salary"
            )

            .orderBy(
                col("net_salary").desc()
            )

            .limit(10)

        )

        application(
            "Top Paid Employees Analytics Generated Successfully."
        )

        return [

            {

                "employee_id": row.employee_id,

                "employee_name": row.employee_name,

                "department_name": row.department_name,

                "net_salary": round(
                    row.net_salary,
                    2
                )

            }

            for row in top_paid.collect()

        ]

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Top Paid Employees Analytics."
        )


# ==========================================================
# Salary Distribution Analytics
# ==========================================================

def salary_distribution_api():

    """
    Department-wise Salary Distribution
    """

    try:

        data = load_data()

        employees = data["employees"]
        departments = data["departments"]
        payroll = data["payroll"]

        salary_distribution = (

            employees

            .join(
                payroll,
                "employee_id"
            )

            .join(
                departments,
                "department_id"
            )

            .groupBy(
                "department_name"
            )

            .agg(
                sum("net_salary").alias(
                    "total_salary"
                )
            )

            .orderBy(
                "department_name"
            )

        )

        application(
            "Salary Distribution Analytics Generated Successfully."
        )

        return [

            {

                "department_name": row.department_name,

                "total_salary": round(
                    row.total_salary,
                    2
                )

            }

            for row in salary_distribution.collect()

        ]

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Salary Distribution Analytics."
        )


# ==========================================================
# Dashboard Charts
# ==========================================================

def dashboard_charts_api():

    """
    Dashboard Chart Data
    """

    try:

        data = load_data()

        employees = data["employees"]
        departments = data["departments"]
        attendance = data["attendance"]
        leave_requests = data["leave_requests"]
        projects = data["projects"]

        # ---------------------------------------------
        # Department Employee Count
        # ---------------------------------------------

        department_chart = (

            employees

            .join(
                departments,
                "department_id"
            )

            .groupBy(
                "department_name"
            )

            .count()

            .orderBy(
                "department_name"
            )

        )

        # ---------------------------------------------
        # Project Status
        # ---------------------------------------------

        project_chart = (

            projects

            .groupBy(
                "status"
            )

            .count()

        )

        # ---------------------------------------------
        # Attendance Status
        # ---------------------------------------------

        attendance_chart = (

            attendance

            .groupBy(
                "status"
            )

            .count()

        )

        # ---------------------------------------------
        # Leave Status
        # ---------------------------------------------

        leave_chart = (

            leave_requests

            .groupBy(
                "status"
            )

            .count()

        )

        application(
            "Dashboard Chart Data Generated Successfully."
        )

        return {

            "department_chart": [

                {

                    "department_name": row.department_name,

                    "employee_count": row["count"]

                }

                for row in department_chart.collect()

            ],

            "project_chart": [

                {

                    "status": row.status,

                    "count": row["count"]

                }

                for row in project_chart.collect()

            ],

            "attendance_chart": [

                {

                    "status": row.status,

                    "count": row["count"]

                }

                for row in attendance_chart.collect()

            ],

            "leave_chart": [

                {

                    "status": row.status,

                    "count": row["count"]

                }

                for row in leave_chart.collect()

            ]

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Generate Dashboard Chart Data."
        )

# ==========================================================
# Run ETL Pipeline
# ==========================================================

def run_etl_pipeline_api():

    """
    Execute CSV ETL Pipeline
    """

    try:

        data = load_data()

        application(
            "CSV ETL Pipeline Executed Successfully."
        )

        return {

            "status": "SUCCESS",

            "message": "CSV files loaded successfully.",

            "datasets": {

                "employees": data["employees"].count(),

                "departments": data["departments"].count(),

                "payroll": data["payroll"].count(),

                "attendance": data["attendance"].count(),

                "leave_requests": data["leave_requests"].count(),

                "projects": data["projects"].count()

            }

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Execute ETL Pipeline."
        )


# ==========================================================
# ETL Status
# ==========================================================

def etl_status_api():

    """
    ETL Status Information
    """

    try:

        data = load_data()

        total_records = (

            data["employees"].count()

            + data["departments"].count()

            + data["payroll"].count()

            + data["attendance"].count()

            + data["leave_requests"].count()

            + data["projects"].count()

        )

        application(
            "ETL Status Retrieved Successfully."
        )

        return {

            "status": "READY",

            "source": "CSV",

            "datasets_loaded": 6,

            "total_records": total_records

        }

    except Exception as e:

        exception(str(e))

        raise DatabaseException(
            "Unable to Fetch ETL Status."
        )