from dataclasses import dataclass

@dataclass
class Actividad:
    plataforma: str

    titulo: str

    ubicacion: str
    url: str
    descripcion: str | None
    imagen: str | None


    precio: float | None
    moneda: str | None
    precio_texto: str | None
    
    duracion: str | None
    fecha: str | None = None


    puntuacion: float | None = None
    cantidad_resenas: int | None = None