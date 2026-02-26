import requests
from typing import Optional
from datetime import datetime, date, timedelta
from app.models.quake.quake_severity import QuakeSeverity
from app.models.earthquake.earthquake_data import EarthquakeData
from app.config.settings import EARTHQUAKE_API_BASE_URL
from app.services.earthquake_mapper import EarthquakeMapper


class EarthquakeService:
    def get_earthquakes_filtered(
        self,
        start_date: str = None,
        end_date: str = None,
        severity: Optional[QuakeSeverity] = None
    ):

        today = date.today().isoformat()
        yesterday = (date.today() - timedelta(days=1)).isoformat()

        start_date = start_date or yesterday
        end_date = end_date or today

        start_dt = datetime.fromisoformat(start_date)
        end_dt = datetime.fromisoformat(end_date)

        if end_dt < start_dt:
            raise ValueError("End date must be greater or equal than start date")

        url = (
            f"{EARTHQUAKE_API_BASE_URL}"
            f"&starttime={start_date}"
            f"&endtime={end_date}"
            f"&orderby=time"
            f"&limit=20000"  # The API service limits queries to 20000, and any that exceed this limit will generate a HTTP response code “400 Bad Request”.
        )

        if severity:
            min_mag, max_mag = EarthquakeMapper.get_magnitude_range(severity)

            if min_mag is not None:
                url += f"&minmagnitude={min_mag}"

            if max_mag is not None:
                url += f"&maxmagnitude={max_mag}"

        print(f"Requesting API URL: {url}")

        # GET
        response = requests.get(url, timeout=120)

        # Check response
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code}")
    
        data = response.json()
        if not data or "features" not in data:
            return EarthquakeData(features=[])

        return EarthquakeData(**data)