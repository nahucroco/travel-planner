import re
from difflib import get_close_matches
import easyocr
from models.traslado import Traslado


_reader = easyocr.Reader(
    ["es", "en"]
)


def _leer_texto(imagen):

    resultado = _reader.readtext(imagen)

    bloques = [
        item[1].strip()
        for item in resultado
    ]

    texto = "\n".join(bloques)

    return texto, bloques


def _obtener_horas(bloques):

    horas = []

    for bloque in bloques:

        match = re.fullmatch(r"\d{1,2}[.:]\d{2}", bloque)

        if match:
            horas.append(
                match.group().replace(".", ":")
            )

    hora_salida = horas[0] if horas else None
    hora_llegada = horas[1] if len(horas) > 1 else None

    return hora_salida, hora_llegada


def _obtener_duracion(bloques):

    for bloque in bloques:

        match = re.search(
            r"\d+h\s*\d+m",
            bloque,
            flags=re.IGNORECASE,
        )

        if match:
            return match.group()

    return None


def _obtener_escalas(bloques):

    for bloque in bloques:

        texto = bloque.lower()

        if "directo" in texto:
            return 0

        match = re.search(r"(\d+)\s*escala", texto)

        if match:
            return int(match.group(1))

        if texto == "escala":
            return 1

    return None


def _obtener_precio(texto):

    match = re.search(
        r"(\d{1,3}(?:\.\d{3})+)",
        texto,
    )

    if not match:
        return None, "ARS", ""

    precio_texto = match.group(1)

    return (
        float(precio_texto.replace(".", "")),
        "ARS",
        f"ARS {precio_texto}",
    )


def _obtener_proveedor(texto):

    proveedores = [
        "Aerolíneas Argentinas",
        "Flybondi",
        "JetSMART",
        "LATAM",
        "Gol",
        "Sky Airline",
    ]

    palabras = re.findall(
        r"[A-Za-zÁÉÍÓÚáéíóúñÑ]+",
        texto
    )

    texto_normalizado = " ".join(palabras)

    for proveedor in proveedores:

        if proveedor.lower() in texto.lower():
            return proveedor

    coincidencia = get_close_matches(
        texto_normalizado,
        proveedores,
        n=1,
        cutoff=0.45
    )

    if coincidencia:
        return coincidencia[0]

    return ""


def _obtener_aeropuertos(bloques):

    bloques = [b.upper().strip() for b in bloques]

    origen = ""
    destino = ""

    for i, bloque in enumerate(bloques):

        if bloque == "IDA":

            if i + 1 < len(bloques):
                siguiente = bloques[i + 1]

                if re.fullmatch(r"[A-Z]{3}", siguiente):
                    origen = siguiente

            if i + 2 < len(bloques):
                siguiente = bloques[i + 2]

                if re.fullmatch(r"[A-Z]{3}", siguiente):
                    destino = siguiente

            break

    return origen, destino


def _obtener_fechas(bloques):

    fechas = []

    for bloque in bloques:

        match = re.search(
            r"(\d{1,2}\s+[A-Za-záéíóúñ]{3,}\.?\s+\d{4})",
            bloque,
            flags=re.IGNORECASE,
        )

        if match:
            fechas.append(match.group(1))

    fecha_ida = fechas[0] if fechas else ""
    fecha_vuelta = fechas[1] if len(fechas) > 1 else None

    return fecha_ida, fecha_vuelta


def obtener_traslado(imagen):

    texto, bloques = _leer_texto(imagen)
    
    print("BLOQUES")
    print("-" * 40)

    for i, bloque in enumerate(bloques):
        print(i, repr(bloque))

    precio, moneda, precio_texto = _obtener_precio(texto)

    origen, destino = _obtener_aeropuertos(bloques)

    fecha_ida, fecha_vuelta = _obtener_fechas(bloques)

    hora_salida, hora_llegada = _obtener_horas(bloques)

    duracion = _obtener_duracion(bloques)

    escalas = _obtener_escalas(texto)

    return Traslado(

        tipo="vuelo",

        plataforma="OCR",

        proveedor=_obtener_proveedor(texto),

        origen=origen,

        destino=destino,

        fecha_salida=fecha_ida,

        hora_salida=hora_salida,

        hora_llegada=hora_llegada,

        duracion=duracion,

        escalas=escalas,

        precio=precio,

        moneda=moneda,

        precio_texto=precio_texto,

    )