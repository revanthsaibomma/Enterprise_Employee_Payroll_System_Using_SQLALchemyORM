"""
==========================================================
File        : transform.py
Project     : Enterprise Employee Payroll
              Management System
Description : ETL Transformation Module
==========================================================
"""

from pyspark.sql.functions import (
    col,
    trim,
    upper,
    initcap,
    when
)


class Transform:

    """
    ======================================================
    Employee Transformation
    ======================================================
    """

    def transform_employees(
        self,
        employees_df
    ):

        employees_df = employees_df.dropDuplicates(
            ["employee_id"]
        )

        employees_df = employees_df.fillna({

            "employee_name": "Unknown",

            "status": "ACTIVE"

        })

        employees_df = employees_df.withColumn(
            "department_id",
            col("department_id").cast("int")
            )

        employees_df = employees_df.withColumn(
            "employee_id",
            col("employee_id").cast("int")
            )

        employees_df = employees_df.withColumn(
            "role_id",
            col("role_id").cast("int")
            )

        return employees_df

    """
    ======================================================
    Department Transformation
    ======================================================
    """

    def transform_departments(
        self,
        departments_df
    ):

        departments_df = departments_df.dropDuplicates(
            ["department_id"]
        )

        departments_df = departments_df.fillna({

            "department_name": "Unknown"

        })

        departments_df = departments_df.withColumn(

            "department_name",

            initcap(

                trim(

                    col("department_name")

                )

            )

        )

        departments_df = departments_df.withColumn(

            "department_id",

            col("department_id").cast("int")

        )

        return departments_df

    """
    ======================================================
    Transform All DataFrames
    ======================================================
    """

    def transform_all(
        self,
        data
    ):

        transformed = {}

        transformed["employees"] = self.transform_employees(

            data["employees"]

        )

        transformed["departments"] = self.transform_departments(

            data["departments"]

        )

        if "payroll" in data:

            transformed["payroll"] = data["payroll"]

        if "attendance" in data:

            transformed["attendance"] = data["attendance"]

        if "leave_requests" in data:

            transformed["leave_requests"] = data["leave_requests"]

        if "projects" in data:

            transformed["projects"] = data["projects"]

        return transformed

"""
======================================================
Payroll Transformation
======================================================
"""

def transform_payroll(
    self,
    payroll_df
):

    payroll_df = payroll_df.dropDuplicates(
        ["payroll_id"]
    )

    payroll_df = payroll_df.fillna({

        "basic_salary": 0,

        "bonus": 0,

        "deduction": 0

    })

    payroll_df = payroll_df.withColumn(

        "payroll_id",

        col("payroll_id").cast("int")

    )

    payroll_df = payroll_df.withColumn(

        "employee_id",

        col("employee_id").cast("int")

    )

    payroll_df = payroll_df.withColumn(

        "basic_salary",

        col("basic_salary").cast("double")

    )

    payroll_df = payroll_df.withColumn(

        "bonus",

        col("bonus").cast("double")

    )

    payroll_df = payroll_df.withColumn(

        "deduction",

        col("deduction").cast("double")

    )

    payroll_df = payroll_df.withColumn(

        "net_salary",

        (
            col("basic_salary") +
            col("bonus") -
            col("deduction")
        ).cast("double")

    )

    return payroll_df


"""
======================================================
Attendance Transformation
======================================================
"""

def transform_attendance(
    self,
    attendance_df
):

    attendance_df = attendance_df.dropDuplicates(
        ["attendance_id"]
    )

    attendance_df = attendance_df.fillna({

        "status": "Absent"

    })

    attendance_df = attendance_df.withColumn(

        "attendance_id",

        col("attendance_id").cast("int")

    )

    attendance_df = attendance_df.withColumn(

        "employee_id",

        col("employee_id").cast("int")

    )

    attendance_df = attendance_df.withColumn(

        "status",

        when(

            upper(trim(col("status"))) == "PRESENT",

            "Present"

        ).otherwise(

            "Absent"

        )

    )

    return attendance_df


"""
======================================================
Leave Request Transformation
======================================================
"""

def transform_leave_requests(
    self,
    leave_df
):

    leave_df = leave_df.dropDuplicates(
        ["leave_id"]
    )

    leave_df = leave_df.fillna({

        "status": "Pending",

        "leave_days": 0

    })

    leave_df = leave_df.withColumn(

        "leave_id",

        col("leave_id").cast("int")

    )

    leave_df = leave_df.withColumn(

        "employee_id",

        col("employee_id").cast("int")

    )

    leave_df = leave_df.withColumn(

        "leave_days",

        col("leave_days").cast("int")

    )

    leave_df = leave_df.withColumn(

        "status",

        when(

            upper(trim(col("status"))) == "APPROVED",

            "Approved"

        ).when(

            upper(trim(col("status"))) == "REJECTED",

            "Rejected"

        ).otherwise(

            "Pending"

        )

    )

    return leave_df


"""
======================================================
Project Transformation
======================================================
"""

def transform_projects(
    self,
    projects_df
):

    projects_df = projects_df.dropDuplicates(
        ["project_id"]
    )

    projects_df = projects_df.fillna({

        "project_budget": 0,

        "status": "Pending"

    })

    projects_df = projects_df.withColumn(

        "project_id",

        col("project_id").cast("int")

    )

    projects_df = projects_df.withColumn(

        "project_budget",

        col("project_budget").cast("double")

    )

    projects_df = projects_df.withColumn(

        "status",

        when(

            upper(trim(col("status"))) == "ACTIVE",

            "Active"

        ).when(

            upper(trim(col("status"))) == "COMPLETED",

            "Completed"

        ).otherwise(

            "Pending"

        )

    )

    return projects_df