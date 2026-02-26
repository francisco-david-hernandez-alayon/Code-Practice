from typing import List

from pydantic import BaseModel

from app.models.tectonic.plate_feature import PlateFeature


class TectonicPlateData(BaseModel):
    type: str
    features: List[PlateFeature]