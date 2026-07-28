"""
==========================================================
File        : load.py
Description : Load Analytics Into Database
==========================================================
"""

from database import get_session

from models.analytics_model import AnalyticsSummary


class Load:

    def save_dashboard(self, metrics):

        session = get_session()

        try:

            summary = AnalyticsSummary(

                **metrics

            )

            session.add(summary)

            session.commit()

            session.refresh(summary)

            return summary

        finally:

            session.close()