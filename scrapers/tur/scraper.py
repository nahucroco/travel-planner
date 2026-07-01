import re

from playwright.sync_api import sync_playwright

from models.actividad import Actividad


def _obtener_titulo(page):
    try:
        return page.locator("h1").first.inner_text().strip()
    except Exception:
        return ""


def _obtener_descripcion(page):
    try:
        body = page.locator("body").inner_text()

        match = re.search(
            r"Guardar\s+Ver las.*?\n(.*?)\nVer más",
            body,
            re.DOTALL,
        )

        if match:
            return " ".join(match.group(1).split())

    except Exception:
        pass

    return ""


def _obtener_imagen(page):

    imagenes = page.locator("img")

    for i in range(imagenes.count()):

        src = imagenes.nth(i).get_attribute("src")

        if (
            src
            and "cloudfront.net/products/" in src
            and "_desktop" in src
        ):
            return src

    return ""


def _obtener_precio(page):

    body = page.locator("body").inner_text()

    match = re.search(
        r"Precio desde\s*([A-Z]{3})\s*([\d\.]+)",
        body,
    )

    if not match:
        return None, None, None

    moneda = match.group(1)

    precio_texto = f"{moneda} {match.group(2)}"

    precio = float(
        match.group(2).replace(".", "")
    )

    return precio, moneda, precio_texto


def _obtener_puntuacion(page):

    body = page.locator("body").inner_text()

    match = re.search(
        r"(\d+\.\d)\s*\((\d+)\s+reseñas\)",
        body,
    )

    if match:
        return float(match.group(1))

    return None


def _obtener_cantidad_resenas(page):

    body = page.locator("body").inner_text()

    match = re.search(
        r"(\d+\.\d)\s*\((\d+)\s+reseñas\)",
        body,
    )

    if match:
        return int(match.group(2))

    return None


def _obtener_duracion(page):

    body = page.locator("body").inner_text()

    match = re.search(
        r"Duración\s+([^\n]+)",
        body,
    )

    if match:
        return match.group(1).strip()

    return ""


def _obtener_ubicacion(page):

    body = page.locator("body").inner_text()

    match = re.search(
        r"Ubicación\s+([^\n]+)",
        body,
    )

    if not match:
        return ""

    ubicacion = match.group(1)

    if ":" in ubicacion:
        ubicacion = ubicacion.split(":", 1)[1].strip()

    return ubicacion


def obtener_actividad(url: str):
    
    print("Entró a obtener_actividad")

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page(
            locale="es-AR",
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
        )

        try:

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000,
            )

            page.wait_for_timeout(4000)

            precio, moneda, precio_texto = _obtener_precio(page)

            return Actividad(
                plataforma="Tur",
                titulo=_obtener_titulo(page),
                descripcion=_obtener_descripcion(page),
                ubicacion=_obtener_ubicacion(page),
                imagen=_obtener_imagen(page),
                url=url,
                precio=precio,
                moneda=moneda,
                precio_texto=precio_texto,
                duracion=_obtener_duracion(page),
                puntuacion=_obtener_puntuacion(page),
                cantidad_resenas=_obtener_cantidad_resenas(page),
            )

        finally:
            browser.close()