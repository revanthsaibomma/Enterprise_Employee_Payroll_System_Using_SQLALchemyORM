"""
==========================================================
File        : spark_session.py
Description : Creates Spark Session
==========================================================
"""

from pyspark.sql import SparkSession

import os

os.environ["HADOOP_HOME"] = r"C:\hadoop"

os.environ["hadoop.home.dir"] = r"C:\hadoop"


def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("EmployeePayrollAnalytics")
        .getOrCreate()
    )

    return spark