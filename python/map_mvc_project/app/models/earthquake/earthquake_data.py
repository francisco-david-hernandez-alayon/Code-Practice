from pydantic import BaseModel
from typing import List

from app.models.earthquake.earthquake_metadata import EarthquakeMetadata
from app.models.earthquake.earthquake_feature import EarthquakeFeature

class EarthquakeData(BaseModel):
    type: str
    metadata: EarthquakeMetadata
    features: List[EarthquakeFeature]