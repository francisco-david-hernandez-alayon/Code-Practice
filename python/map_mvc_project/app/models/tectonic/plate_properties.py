from typing import Optional
from pydantic import BaseModel


class PlateProperties(BaseModel):
    LAYER: Optional[str] = None
    Name: Optional[str] = None
    Source: Optional[str] = None
    PlateA: Optional[str] = None
    PlateB: Optional[str] = None
    Type: Optional[str] = None