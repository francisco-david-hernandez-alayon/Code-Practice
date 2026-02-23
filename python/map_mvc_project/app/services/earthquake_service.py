import requests
from datetime import datetime, date, timedelta

from app.config.settings import EARTHQUAKE_API_BASE_URL
from app.models.earthquake.earthquake_data import EarthquakeData


class EarthquakeService:

    def get_earthquakes_filtered(
    self,
    start_date: str = None,
    end_date: str = None,
        severity: str = None
    ):

        today = date.today().isoformat()
        yesterday = (date.today() - timedelta(days=1)).isoformat()

        start_date = start_date or yesterday
        end_date = end_date or today

        # Data validation
        start_dt = datetime.fromisoformat(start_date)
        end_dt = datetime.fromisoformat(end_date)

        if end_dt < start_dt:
            raise ValueError("End date must be greater or equal than start date")

        url = (
            f"{EARTHQUAKE_API_BASE_URL}"
            f"&starttime={start_date}"
            f"&endtime={end_date}"
            f"&orderby=time"
        )

        print(f"Requesting API URL: {url}")

        response = requests.get(url)
        response.raise_for_status()

        return EarthquakeData(**response.json())
