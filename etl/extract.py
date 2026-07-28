from etl.spark_session import create_spark_session

import os

print(os.getcwd())


class Extract:

    def __init__(self):

        self.spark = create_spark_session()

    def extract_all(self):

        return {

            "employees":

                self.spark.read.csv(
                    "data/employees.csv",
                    header=True,
                    inferSchema=True
                ),

            "departments":

                self.spark.read.csv(
                    "data/departments.csv",
                    header=True,
                    inferSchema=True
                ),

            "attendance":

                self.spark.read.csv(
                    "data/attendance.csv",
                    header=True,
                    inferSchema=True
                ),

            "leave_requests":

                self.spark.read.csv(
                    "data/leave_requests.csv",
                    header=True,
                    inferSchema=True
                ),

            "payroll":

                self.spark.read.csv(
                    "data/payroll.csv",
                    header=True,
                    inferSchema=True
                ),

            "projects":

                self.spark.read.csv(
                    "data/projects.csv",
                    header=True,
                    inferSchema=True
                )

        }