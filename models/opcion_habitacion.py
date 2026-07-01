from dataclasses import dataclass

@dataclass
class OpcionHabitacion:
    nombre: str
    capacidad: int | None
    precio: float | None
    moneda: str | None
    precio_texto: str

    desayuno_incluido: bool | None = None
    cancelacion_gratis: bool | None = None
    requiere_tarjeta: bool | None = None