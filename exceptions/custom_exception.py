"""
==========================================================
File        : custom_exception.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Custom Exception Classes
==========================================================
"""


# ==========================================================
# Base Exception
# ==========================================================

class EmployeePayrollException(Exception):
    """
    Base Exception Class
    """

    def __init__(self, message):

        super().__init__(message)

        self.message = message

    def __str__(self):

        return self.message


# ==========================================================
# Validation Exception
# ==========================================================

class ValidationException(EmployeePayrollException):
    """
    Raised when validation fails.
    """

    pass


# ==========================================================
# Database Exception
# ==========================================================

class DatabaseException(EmployeePayrollException):
    """
    Raised when database operation fails.
    """

    pass


# ==========================================================
# Employee Exception
# ==========================================================

class EmployeeException(EmployeePayrollException):
    """
    Raised for Employee related errors.
    """

    pass


# ==========================================================
# Department Exception
# ==========================================================

class DepartmentException(EmployeePayrollException):
    """
    Raised for Department related errors.
    """

    pass


# ==========================================================
# Role Exception
# ==========================================================

class RoleException(EmployeePayrollException):
    """
    Raised for Role related errors.
    """

    pass


# ==========================================================
# Attendance Exception
# ==========================================================

class AttendanceException(EmployeePayrollException):
    """
    Raised for Attendance related errors.
    """

    pass


# ==========================================================
# Leave Exception
# ==========================================================

class LeaveException(EmployeePayrollException):
    """
    Raised for Leave related errors.
    """

    pass


# ==========================================================
# Project Exception
# ==========================================================

class ProjectException(EmployeePayrollException):
    """
    Raised for Project related errors.
    """

    pass


# ==========================================================
# Task Exception
# ==========================================================

class TaskException(EmployeePayrollException):
    """
    Raised for Task related errors.
    """

    pass


# ==========================================================
# Salary Exception
# ==========================================================

class SalaryException(EmployeePayrollException):
    """
    Raised for Salary related errors.
    """

    pass


# ==========================================================
# Payroll Exception
# ==========================================================

class PayrollException(EmployeePayrollException):
    """
    Raised for Payroll related errors.
    """

    pass


# ==========================================================
# Report Exception
# ==========================================================

class ReportException(EmployeePayrollException):
    """
    Raised for Report generation errors.
    """

    pass


# ==========================================================
# Duplicate Record Exception
# ==========================================================

class DuplicateRecordException(EmployeePayrollException):
    """
    Raised when duplicate records are found.
    """

    pass


# ==========================================================
# Record Not Found Exception
# ==========================================================

class RecordNotFoundException(EmployeePayrollException):
    """
    Raised when a record is not found.
    """

    pass


# ==========================================================
# Authentication Exception
# ==========================================================

class AuthenticationException(EmployeePayrollException):
    """
    Raised for authentication failures.
    """

    pass


# ==========================================================
# Authorization Exception
# ==========================================================

class AuthorizationException(EmployeePayrollException):
    """
    Raised for authorization failures.
    """

    pass