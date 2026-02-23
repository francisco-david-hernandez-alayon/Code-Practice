from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import folium

from app.views.map_renderer import add_markers
from app.services.earthquake_service import EarthquakeService
from app.services.earthquake_mapper import EarthquakeMapper

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def show_map(
    request: Request,
    start_date: str = Query(None),
    end_date: str = Query(None),
    severity: str = Query(None)
):
    earthquake_service = EarthquakeService()
    earthquake_mapper = EarthquakeMapper()

    # Create folium map
    m = folium.Map(location=[0, 0], zoom_start=3)

    # Get point
    earthquake_data = earthquake_service.get_earthquakes_filtered(start_date, end_date, severity)
    quake_points = earthquake_mapper.to_quake_points(earthquake_data)
    quake_count = len(quake_points)  
    
    # Add points to the map
    add_markers(m, quake_points)

    # Return and render map
    map_html = m._repr_html_()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "map": map_html,
            "quake_count": quake_count
        }
    )



