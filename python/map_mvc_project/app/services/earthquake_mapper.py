from datetime import datetime, timezone

from app.models.quake.quake_point import QuakePoint
from app.models.earthquake.earthquake_data import EarthquakeData
from app.models.quake.quake_severity import QuakeSeverity

class EarthquakeMapper:

    from datetime import datetime


    @staticmethod
    def earthQuaketimestamp_to_date(timestamp: int) -> str:
        if timestamp is None:
            return ""

        return datetime.fromtimestamp(
            timestamp / 1000,
            tz=timezone.utc
        ).isoformat()

    @staticmethod
    def get_severity(magnitude: float):
        if magnitude is None:
            return QuakeSeverity.MICRO

        if magnitude < 2.5:
            return QuakeSeverity.MICRO

        if magnitude < 4.0:
            return QuakeSeverity.LIGHT

        if magnitude < 5.5:
            return QuakeSeverity.MODERATE

        if magnitude < 7.0:
            return QuakeSeverity.STRONG

        return QuakeSeverity.VERY_STRONG


    @staticmethod
    def to_quake_points(earthquake_data: EarthquakeData):

        points = []

        for feature in earthquake_data.features:

            coords = feature.geometry.coordinates

            # GeoJSON order = [lon, lat, depth]
            longitude = coords[0]
            latitude = coords[1]

            points.append(
                QuakePoint(
                    latitude=latitude,
                    longitude=longitude,
                    magnitude=feature.properties.mag,
                    place=feature.properties.place,
                    date=EarthquakeMapper.earthQuaketimestamp_to_date(feature.properties.time) 
                )
            )

        return points