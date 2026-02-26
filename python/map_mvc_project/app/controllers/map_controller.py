from typing import Optional

from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import folium

from app.models.quake.quake_severity import QuakeSeverity
from app.services.tectonic_plate_service import TectonicPlateService
from app.views.map_renderer import add_lines, add_markers
from app.services.earthquake_service import EarthquakeService
from app.services.earthquake_mapper import EarthquakeMapper

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def show_map(
    request: Request,
    start_date: str = Query(None),
    end_date: str = Query(None),
    severity: str = Query(None),
    show_plates: bool = Query(False)
):
    error_message = None
    earthquake_service = EarthquakeService()
    earthquake_mapper = EarthquakeMapper()
    tectonic_plate_service = TectonicPlateService()

    try:
        # Create folium map
        m = folium.Map(location=[0, 0], zoom_start=3)

        # Get point
        earthquake_data = earthquake_service.get_earthquakes_filtered(start_date, end_date, severity)
        
        quake_points = earthquake_mapper.to_quake_points(earthquake_data)
        quake_count = len(quake_points)  
        
        # Add points to the map
        add_markers(m, quake_points)

        # Tectonic Plates (optional)
        if show_plates:
            plate_data = tectonic_plate_service.get_tectonic_plates()
            add_lines(m, plate_data)

        # Return and render map
        map_html = m._repr_html_()

    except Exception as e:
        error_message = str(e)
        quake_count = 0
        map_html = None
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "map": map_html,
            "quake_count": quake_count,

            "start_date": start_date,
            "end_date": end_date,

            "error_message": error_message
        }
    )



