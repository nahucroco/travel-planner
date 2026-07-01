import re

from playwright.sync_api import sync_playwright

from models.alojamiento import Alojamiento
from models.opcion_habitacion import OpcionHabitacion


def _obtener_titulo(page):
    try:
        texto = page.locator("h1").first.inner_text().strip()

        match = re.search(r"Ofertas en (.+?) \(", texto)

        if match:
            return match.group(1)

        return texto

    except Exception:
        return ""


def _obtener_ubicacion(page):
    try:
        texto = (
            page
            .locator('[data-testid="PropertyHeaderAddressDesktop-wrapper"]')
            .inner_text()
            .strip()
        )

        return texto.split("\n")[0]

    except Exception:
        return ""


def _obtener_imagen(page):

    imagenes = page.locator("img")

    for i in range(imagenes.count()):

        src = imagenes.nth(i).get_attribute("src")

        if (
            src
            and "cf.bstatic.com/xdata/images/hotel/" in src
        ):
            return src

    return ""


def _obtener_puntuacion(page):
    try:
        texto = (
            page
            .locator('[data-testid="review-score-component"]')
            .inner_text()
        )

        match = re.search(r"(\d+[.,]\d+)", texto)

        if match:
            return float(match.group(1).replace(",", "."))

    except Exception:
        pass

    return None


def _obtener_cantidad_resenas(page):
    try:
        texto = (
            page
            .locator('[data-testid="review-score-component"]')
            .inner_text()
        )

        match = re.search(r"(\d+)\s+comentarios", texto)

        if match:
            return int(match.group(1))

    except Exception:
        pass

    return None


def _obtener_tipo_alojamiento(page):
    try:
        texto = page.locator("h1").first.inner_text()

        match = re.search(r"\((.*?)\)", texto)

        if match:
            return match.group(1)

    except Exception:
        pass

    return ""


def _obtener_opciones_habitaciones(page):

    opciones = []

    filas = page.locator("tr.js-rt-block-row")

    for i in range(filas.count()):

        fila = filas.nth(i)

        # --------------------------
        # Nombre
        # --------------------------

        try:
            nombre = (
                fila
                .locator(".hprt-roomtype-icon-link")
                .inner_text()
                .strip()
            )
        except Exception:
            nombre = ""

        # --------------------------
        # Capacidad
        # --------------------------

        try:
            texto_capacidad = (
                fila
                .locator(".bui-u-sr-only")
                .first
                .inner_text()
                .strip()
            )

            match = re.search(r"(\d+)", texto_capacidad)

            capacidad = int(match.group(1)) if match else None

        except Exception:
            capacidad = None

        # --------------------------
        # Precio
        # --------------------------

        try:
            precio_texto = (
                fila
                .locator(".bui-price-display__value")
                .inner_text()
                .replace("\xa0", " ")
                .strip()
            )

            match = re.search(r"([\d.]+)", precio_texto)

            precio = (
                float(match.group(1).replace(".", ""))
                if match else None
            )

            moneda = "ARS"

        except Exception:
            precio = None
            moneda = None
            precio_texto = ""

        opciones.append(
            OpcionHabitacion(
                nombre=nombre,
                capacidad=capacidad,
                precio=precio,
                moneda=moneda,
                precio_texto=precio_texto,
            )
        )

    return opciones


def _seleccionar_opcion(opciones):

    if not opciones:
        return None

    # Por ahora elegimos la habitación más barata.
    return min(opciones, key=lambda o: o.precio or float("inf"))


def obtener_alojamiento(
    url: str,
    check_in: str,
    check_out: str,
    viajeros: int,
):

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

            page.wait_for_timeout(5000)

            opciones = _obtener_opciones_habitaciones(page)

            opcion = _seleccionar_opcion(opciones)

            if opcion is None:
                return None

            return Alojamiento(
                plataforma="Booking",
                titulo=_obtener_titulo(page),
                tipo_alojamiento=_obtener_tipo_alojamiento(page),
                ubicacion=_obtener_ubicacion(page),
                imagen=_obtener_imagen(page),
                url=url,
                precio=opcion.precio,
                moneda=opcion.moneda,
                precio_texto=opcion.precio_texto,
                check_in=check_in,
                check_out=check_out,
                viajeros=viajeros,
                noches=None,
                puntuacion=_obtener_puntuacion(page),
                cantidad_resenas=_obtener_cantidad_resenas(page),
            )

        finally:
            browser.close()