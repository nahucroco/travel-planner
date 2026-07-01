from scrapers.airbnb.scraper import obtener_alojamiento as obtener_airbnb
from scrapers.booking.scraper import obtener_alojamiento as obtener_booking
from scrapers.tur.scraper import obtener_actividad


def obtener_datos_alojamiento(
    url: str,
    check_in: str,
    check_out: str,
    viajeros: int,
):

    url_lower = url.lower()

    if "airbnb." in url_lower:
        print("AIRBNB")
        return obtener_airbnb(
            base_url=url,
            check_in=check_in,
            check_out=check_out,
            viajeros=viajeros,
        )

    if "booking." in url_lower:
        print("BOOKING")
        return obtener_booking(
            url=url,
            check_in=check_in,
            check_out=check_out,
            viajeros=viajeros,
        )
    
    if "tur.com" in url_lower:
        print("TUR")
        return obtener_actividad(url)
    
    if "despegar." in url_lower:
        raise ValueError(
            "Todavía no se soportan URLs de Despegar."
        )
    
    print("NO SOPORTADA")

    raise ValueError("Plataforma no soportada")