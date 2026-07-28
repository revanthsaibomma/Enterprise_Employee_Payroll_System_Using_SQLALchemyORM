"""
==========================================================
File        : charts.py
Project     : Enterprise Employee Project and Payroll
              Management System
Description : Plotly Chart Generator
==========================================================
"""

import plotly.express as px


class ChartGenerator:

    @staticmethod
    def employee_department_chart(data):

        fig = px.bar(

            data,

            x="department_name",

            y="employee_count",

            title="Employees by Department"

        )

        return fig.to_json()


    @staticmethod
    def salary_distribution_chart(data):

        fig = px.bar(

            data,

            x="department_name",

            y="total_salary",

            title="Salary Distribution"

        )

        return fig.to_json()


    @staticmethod
    def attendance_chart(data):

        fig = px.pie(

            data,

            names="status",

            values="count",

            title="Attendance Status"

        )

        return fig.to_json()


    @staticmethod
    def leave_chart(data):

        fig = px.pie(

            data,

            names="status",

            values="count",

            title="Leave Status"

        )

        return fig.to_json()


    @staticmethod
    def project_status_chart(data):

        fig = px.pie(

            data,

            names="status",

            values="count",

            title="Project Status"

        )

        return fig.to_json()


    @staticmethod
    def top_paid_chart(data):

        fig = px.bar(

            data,

            x="employee_name",

            y="net_salary",

            title="Top Paid Employees"

        )

        return fig.to_json()