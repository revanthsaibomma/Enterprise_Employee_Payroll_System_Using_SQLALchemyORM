"""
==========================================================
File        : dashboard.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Analytics Dashboard
==========================================================
"""

from visualization.charts import ChartGenerator


class Dashboard:

    @staticmethod
    def build_dashboard(

        employee_data,

        salary_data,

        attendance_data,

        leave_data,

        project_data,

        top_paid_data

    ):

        return {

            "employee_chart":

                ChartGenerator.employee_department_chart(

                    employee_data

                ),

            "salary_chart":

                ChartGenerator.salary_distribution_chart(

                    salary_data

                ),

            "attendance_chart":

                ChartGenerator.attendance_chart(

                    attendance_data

                ),

            "leave_chart":

                ChartGenerator.leave_chart(

                    leave_data

                ),

            "project_chart":

                ChartGenerator.project_status_chart(

                    project_data

                ),

            "top_paid_chart":

                ChartGenerator.top_paid_chart(

                    top_paid_data

                )

        }