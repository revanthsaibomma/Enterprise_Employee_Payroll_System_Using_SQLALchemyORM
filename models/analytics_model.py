"""
==========================================================
File        : analytics_model.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Analytics Summary Model
==========================================================
"""

from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime
)

from datetime import datetime

from database import Base


class AnalyticsSummary(Base):

    __tablename__ = "analytics_summary"

    analytics_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    total_employees = Column(
        Integer,
        nullable=False,
        default=0
    )

    active_employees = Column(
        Integer,
        nullable=False,
        default=0
    )

    inactive_employees = Column(
        Integer,
        nullable=False,
        default=0
    )

    total_departments = Column(
        Integer,
        nullable=False,
        default=0
    )

    total_projects = Column(
        Integer,
        nullable=False,
        default=0
    )

    active_projects = Column(
        Integer,
        nullable=False,
        default=0
    )

    completed_projects = Column(
        Integer,
        nullable=False,
        default=0
    )

    pending_projects = Column(
        Integer,
        nullable=False,
        default=0
    )

    total_payroll = Column(
        Float,
        nullable=False,
        default=0.0
    )

    average_salary = Column(
        Float,
        nullable=False,
        default=0.0
    )

    highest_salary = Column(
        Float,
        nullable=False,
        default=0.0
    )

    lowest_salary = Column(
        Float,
        nullable=False,
        default=0.0
    )

    attendance_percentage = Column(
        Float,
        nullable=False,
        default=0.0
    )

    approved_leaves = Column(
        Integer,
        nullable=False,
        default=0
    )

    pending_leaves = Column(
        Integer,
        nullable=False,
        default=0
    )

    rejected_leaves = Column(
        Integer,
        nullable=False,
        default=0
    )

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return (
            f"<AnalyticsSummary("
            f"{self.analytics_id})>"
        )