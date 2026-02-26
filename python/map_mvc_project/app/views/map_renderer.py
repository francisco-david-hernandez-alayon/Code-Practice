import folium

from app.models.quake.quake_severity import QuakeSeverity
from app.services.earthquake_mapper import EarthquakeMapper


SEVERITY_COLOR_MAP = {
    QuakeSeverity.MICRO: "green",
    QuakeSeverity.LIGHT: "yellow",
    QuakeSeverity.MODERATE: "orange",
    QuakeSeverity.STRONG: "red",
    QuakeSeverity.VERY_STRONG: "black",
}


def add_markers(map_object, quake_points):

    for quake in quake_points:
        severity = EarthquakeMapper.get_severity(quake.magnitude)
        color = SEVERITY_COLOR_MAP.get(severity, "gray")

        text = f"""
        Magnitude: {quake.magnitude or 'N/A'}<br>
        Place: {quake.place or 'Unknown'}<br>
        Date: {quake.date or ''}
        """

        folium.CircleMarker(
            location=[quake.latitude, quake.longitude],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            tooltip=text
        ).add_to(map_object)


def add_lines(map_object, plate_data):

    for feature in plate_data.features:

        geometry = feature.geometry

        if geometry.type != "LineString":
            continue

        folium.PolyLine(
            locations=[(lat, lon) for lon, lat in geometry.coordinates],
            weight=2,
            color="blue",
            opacity=0.6
        ).add_to(map_object)