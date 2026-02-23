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


from folium.plugins import MarkerCluster


def add_markers(map_object, quake_points):

    marker_cluster = MarkerCluster(
        max_cluster_radius=20,
        spiderfy_distance_multiplier=2
    ).add_to(map_object)

    for quake in quake_points:

        text = f"""
        Magnitude: {quake.magnitude or 'N/A'}<br>
        Place: {quake.place or 'Unknown'}<br>
        Date: {quake.date or ''}
        """

        folium.CircleMarker(
            location=[quake.latitude, quake.longitude],
            radius=5,
            color="red",
            fill=True,
            fill_color="red",
            tooltip=text
        ).add_to(marker_cluster)