from dataclasses import dataclass

@dataclass
class Alojamiento:
    plataforma: str
    titulo: str
    ubicacion: str
    tipo_alojamiento: str
    imagen: str
    url: str

    precio: float
    moneda: str
    precio_texto: str

    check_in: str
    check_out: str

    viajeros: int | None = None
    noches: int | None = None
    puntuacion: float | None = None
    cantidad_resenas: int | None = None