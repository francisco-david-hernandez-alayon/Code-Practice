import requests

from app.config.settings import TECTONIC_PLATES_URL
from app.models.tectonic.tectonic_plate_data import TectonicPlateData



class TectonicPlateService:

    def get_tectonic_plates(self) -> TectonicPlateData:

        print(f"Requesting Tectonic Plates API URL: {TECTONIC_PLATES_URL}")

        response = requests.get(TECTONIC_PLATES_URL, timeout=10)

        if response.status_code != 200:
            raise Exception(f"Tectonic Plates API Error: {response.status_code}")

        data = response.json()

        if not data or "features" not in data:
            return TectonicPlateData(features=[])

        return TectonicPlateData(**data)