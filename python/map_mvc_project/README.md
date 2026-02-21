# Proyecto python
Autor: Francisco David Hernández Alayón

<br>

## Configuración de proyecto en linux
Instalar entorno virtual python 
```
sudo apt update
sudo apt install python3-venv
```

```
python -m venv venv
```

Crear entorno virtual
```
python3 -m venv venv
```

Activar entorno virtual
```
source venv/bin/activate
```

Instalar dependencias(después de activar el entorno virtual)
```
pip install -r requirements.txt
```

### Dependencias

- **FastAPI**  
  Framework web moderno para construir APIs y aplicaciones backend en Python basado en ASGI.  
  Permite definir rutas HTTP y manejar solicitudes y respuestas.

- **Uvicorn**  
  Servidor ASGI ligero para ejecutar aplicaciones compatibles como FastAPI.  
  Gestiona conexiones HTTP de forma asíncrona.

- **Jinja2**  
  Motor de plantillas para generar HTML dinámico desde Python.  
  Permite insertar variables y estructuras de control en archivos HTML.

- **Folium**  
  Librería Python para crear mapas interactivos basados en Leaflet.js.  
  Genera visualizaciones geográficas en formato HTML.

- **Requests**  
  Librería HTTP para realizar peticiones a servicios externos.  
  Facilita el consumo de APIs REST y manejo de respuestas JSON.

- **python-multipart**  
  Librería para procesar datos `multipart/form-data`.  
  Permite manejar formularios y subida de archivos en aplicaciones web.
  
<br>

## Ejecutar aplicación en linux
Activar entorno virtual
```
source venv/bin/activate
```

En raíz de directorio:
```
uvicorn main:app --reload
```