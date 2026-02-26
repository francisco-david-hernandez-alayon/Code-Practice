from pydantic import BaseModel
from typing import List, Optional


class PlateGeometry(BaseModel):
    type: str
    coordinates: List[List[float]]