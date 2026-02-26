from datetime import datetime, timezone

from app.models.quake.quake_point import QuakePoint
from app.models.earthquake.earthquake_data import EarthquakeData
from app.models.quake.quake_severity import QuakeSeverity

class EarthquakeMapper:

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
    def get_magnitude_range(severity: QuakeSeverity):

        # ensure QuakeSeverity enum
        if isinstance(severity, str):
            severity = QuakeSeverity(severity)

        if severity == QuakeSeverity.MICRO:
            return (0, 2.4)
        if severity == QuakeSeverity.LIGHT:
            return (2.5, 3.9)
        if severity == QuakeSeverity.MODERATE:
            return (4.0, 5.4)
        if severity == QuakeSeverity.STRONG:
            return (5.5, 6.9)
        if severity == QuakeSeverity.VERY_STRONG:
            return (7.0, None)

        return (None, None)

    @staticmethod
    def to_quake_points(earthquake_data: EarthquakeData):

        points = []

        for feature in earthquake_data.features:
            
            try:
                coords = feature.geometry.coordinates

                if not coords or len(coords) < 2:
                    print(f"invalid coordinade(len < 2)")
                    continue

                # GeoJSON order = [lon, lat, depth]
                longitude = float(coords[0]) if coords[0] is not None else None
                latitude = float(coords[1]) if coords[1] is not None else None
                
                if longitude is None or latitude is None: # Skip invalid coordinates
                    print(f"invalid coordinade: {longitude}, {latitude}")
                    continue

                points.append(
                    QuakePoint(
                        latitude=latitude,
                        longitude=longitude,
                        magnitude=feature.properties.mag,
                        place=feature.properties.place,
                        date=EarthquakeMapper.earthQuaketimestamp_to_date(feature.properties.time) 
                    )
                )

            except Exception as e:
                print(f"Error transforming point: " + e)
                continue


        return points