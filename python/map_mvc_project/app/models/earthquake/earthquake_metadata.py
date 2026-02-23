from pydantic import BaseModel

class EarthquakeMetadata(BaseModel):
    generated: int
    url: str
    title: str
    status: int
    api: str
    count: int
