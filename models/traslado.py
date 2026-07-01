from dataclasses import dataclass

@dataclass
class Traslado:

    tipo: str

    plataforma: str

    proveedor: str

    origen: str
    destino: str

    fecha_salida: str

    hora_salida: str | None = None
    hora_llegada: str | None = None

    duracion: str | None = None

    escalas: int | None = None

    precio: float | None = None
    moneda: str | None = None
    precio_texto: str | None = None