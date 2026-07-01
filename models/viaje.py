from dataclasses import dataclass

@dataclass
class Viaje:

    id: str

    titulo: str

    destino: str

    fecha_inicio: str

    fecha_fin: str

    viajeros: int

    hospedajes: list

    actividades: list

    traslados: list