from pydantic import BaseModel
from typing import Optional

class QuakePoint(BaseModel):
    latitude: float
    longitude: float
    magnitude: Optional[float] = None
    place: Optional[str] = None
    date: Optional[str] = None