from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import folium

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def show_map(request: Request):
    m = folium.Map(location=[40.4168, -3.7038], zoom_start=13)
    map_html = m._repr_html_()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "map": map_html}
    )