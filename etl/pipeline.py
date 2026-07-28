"""
==========================================================
File        : pipeline.py
Description : ETL Pipeline
==========================================================
"""

from etl.extract import Extract

from etl.transform import Transform

from etl.load import Load


class ETLPipeline:

    def __init__(self):

        self.extract = Extract()

        self.transform = Transform()

        self.load = Load()

    def run(self):

        data = self.extract.extract_all()

        metrics = self.transform.dashboard_metrics(

            data

        )

        dashboard = self.load.save_dashboard(

            metrics

        )

        return {

            "status": "SUCCESS",

            "dashboard_id":

                dashboard.analytics_id

        }