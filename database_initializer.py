"""
==========================================================
File        : database_initializer.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Creates all database tables
==========================================================
"""

from sqlalchemy.exc import SQLAlchemyError

from database import (
    Base,
    engine
)

# ==========================================================
# Import All ORM Models
# ==========================================================

from models.department_model import Department
from models.role_model import Role
from models.employee_model import Employee
from models.attendance_model import Attendance
from models.leave_model import LeaveRequest
from models.project_model import Project
from models.employee_project_model import EmployeeProject
from models.task_model import Task
from models.salary_model import Salary
from models.payroll_model import Payroll


# ==========================================================
# Create Database Tables
# ==========================================================

def create_tables():
    """
    Creates all tables if they do not exist.
    """

    try:

        print("\n" + "=" * 70)

        print("CREATING DATABASE TABLES")

        print("=" * 70)

        Base.metadata.create_all(bind=engine)

        print("\nAll Database Tables Created Successfully.")

    except SQLAlchemyError as error:

        print("\nUnable to Create Database Tables.")

        print(f"Database Error : {error}")

        raise

    except Exception as error:

        print("\nUnexpected Error While Creating Tables.")

        print(error)

        raise

    finally:

        print("\nDatabase Initialization Completed.")

# ==========================================================
# Drop Database Tables
# ==========================================================


def drop_tables():
    """
    Drops all tables.
    """

    try:

        print("\n" + "=" * 70)

        print("DROPPING DATABASE TABLES")

        print("=" * 70)

        Base.metadata.drop_all(bind=engine)

        print("\nAll Database Tables Dropped Successfully.")

    except SQLAlchemyError as error:

        print("\nUnable to Drop Tables.")

        print(error)

        raise

    except Exception as error:

        print("\nUnexpected Error.")

        print(error)

        raise

    finally:

        print("\nDrop Table Operation Completed.")

# ==========================================================
# Recreate Tables
# ==========================================================


def recreate_tables():
    """
    Drops all existing tables and recreates them.
    """

    try:

        drop_tables()

        create_tables()

        print("\nDatabase Recreated Successfully.")

    except Exception as error:

        print("\nDatabase Recreation Failed.")

        print(error)

# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    create_tables()