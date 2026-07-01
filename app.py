import os
import tempfile
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, HTTPException, UploadFile
from models.request_scrape import ScrapeRequest
from models.request_ocr import OCRRequest
from scrapers.despegar.scraper import obtener_traslado
from services.scraper_service import obtener_datos_alojamiento

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/scrape")
def scrape(request: ScrapeRequest):
    
    print(request.url)

    try:
        alojamiento = obtener_datos_alojamiento(
            url=request.url,
            check_in=request.check_in,
            check_out=request.check_out,
            viajeros=request.viajeros,
        )

        if alojamiento is None:
            raise HTTPException(
                status_code=500,
                detail="No se pudo obtener información del alojamiento."
            )

        return alojamiento.__dict__

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/ocr/vuelo")
async def ocr_vuelo(
    imagen: UploadFile = File(...)
):
    archivo_temporal = None

    try:
        # Crear archivo temporal conservando la extensión
        extension = os.path.splitext(imagen.filename)[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as temp:

            archivo_temporal = temp.name
            temp.write(await imagen.read())

        vuelo = obtener_traslado(archivo_temporal)

        if vuelo is None:
            raise HTTPException(
                status_code=500,
                detail="No se pudo obtener información del vuelo."
            )

        return vuelo.__dict__

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    finally:
        if archivo_temporal and os.path.exists(archivo_temporal):
            os.remove(archivo_temporal)