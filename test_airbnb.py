from scrapers.airbnb.scraper import obtener_alojamiento

resultado = obtener_alojamiento(
    base_url="https://www.airbnb.com.ar/rooms/1463245810949100943",
    check_in="2027-01-03",
    check_out="2027-01-08",
    viajeros=4,
)

print(resultado)