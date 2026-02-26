from pydantic import BaseModel

from app.models.tectonic.plate_geometry import PlateGeometry
from app.models.tectonic.plate_properties import PlateProperties

class PlateFeature(BaseModel):
    type: str
    properties: PlateProperties
    geometry: PlateGeometry