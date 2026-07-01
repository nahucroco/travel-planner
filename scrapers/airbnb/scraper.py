import re

from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError,
)

from models.alojamiento import Alojamiento


from urllib.parse import urlencode


def _armar_url(
    base_url,
    check_in,
    check_out,
    viajeros,
):

    params = {
        "check_in": check_in,
        "check_out": check_out,
        "guests": viajeros,
        "adults": viajeros
    }

    return f"{base_url}?{urlencode(params)}"

def _obtener_precio(page):
    patron = r"\$\s*([\d,.]+)\s*([A-Z]{3})"

    try:
        info = page.locator(
            '[data-testid="book-it-default"] span[aria-label]'
        ).get_attribute("aria-label")

        if info:
            match = re.search(patron, info)
            if match:
                return (
                    float(match.group(1).replace(",", "")),
                    match.group(2),
                    match.group(0).replace("\xa0", " ").strip(),
                )
    except Exception:
        pass

    spans = page.locator('[data-testid="book-it-default"] span')

    for i in range(spans.count()):
        texto = spans.nth(i).inner_text().replace("\xa0", " ").strip()

        match = re.search(patron, texto)

        if match:
            return (
                float(match.group(1).replace(",", "")),
                match.group(2),
                match.group(0).replace("\xa0", " ").strip(),
            )

    return None, None, None

def _obtener_titulo(page):
    try:
        return page.locator("h1").first.inner_text().strip()
    except Exception:
        return ""

def _obtener_tipo_y_ubicacion(page):
    try:
        texto = page.locator("h2").first.inner_text().strip()

        if " en " in texto:
            tipo, ubicacion = texto.split(" en ", 1)
            return tipo, ubicacion

        return "", texto

    except Exception:
        return "", ""

def _obtener_imagenes(page):
    imagenes = []

    for i in range(page.locator("img").count()):
        src = page.locator("img").nth(i).get_attribute("src")

        if src:
            imagenes.append(src)

    return imagenes


def _obtener_imagen(page):
    for src in _obtener_imagenes(page):

        if "/hosting/Hosting-" in src and "/original/" in src:
            return src

    return ""

def obtener_alojamiento(
    base_url: str,
    check_in: str,
    check_out: str,
    viajeros: int | None = None,
) -> Alojamiento:

    url = _armar_url(base_url, check_in, check_out, viajeros)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

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

            page.locator(
                '[data-testid="book-it-default"]'
            ).wait_for(timeout=15000)

            precio, moneda, precio_texto = _obtener_precio(page)
            tipo_alojamiento, ubicacion = _obtener_tipo_y_ubicacion(page)

            return Alojamiento(
                plataforma="Airbnb",
                titulo=_obtener_titulo(page),
                tipo_alojamiento=tipo_alojamiento,
                ubicacion=ubicacion,
                imagen=_obtener_imagen(page),
                url=url,
                precio=precio,
                moneda=moneda,
                precio_texto=precio_texto,
                check_in=check_in,
                check_out=check_out,
                viajeros=viajeros,
            )

        except PlaywrightTimeoutError:
            return None

        finally:
            browser.close()