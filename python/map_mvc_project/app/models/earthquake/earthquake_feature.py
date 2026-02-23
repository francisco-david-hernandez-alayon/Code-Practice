from pydantic import BaseModel
from typing import Optional
from typing import List, Optional

class Geometry(BaseModel):
    type: str
    coordinates: List[float]  # [longitude, latitude, depth]


class Properties(BaseModel):
    mag: Optional[float]
    place: Optional[str]
    time: int
    updated: Optional[int]
    url: Optional[str]
    detail: Optional[str]
    felt: Optional[int]
    cdi: Optional[float]
    mmi: Optional[float]
    alert: Optional[str]
    status: Optional[str]
    tsunami: Optional[int]
    sig: Optional[int]
    net: Optional[str]
    code: Optional[str]
    magType: Optional[str]
    type: Optional[str]
    title: Optional[str]


class EarthquakeFeature(BaseModel):
    type: str
    properties: Properties
    geometry: Geometry
    id: str