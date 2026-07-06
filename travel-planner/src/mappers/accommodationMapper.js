export function mapScrapedAccommodation(scraped, tripId) {
    return {
        trip: tripId,

        platform: scraped.plataforma?.toUpperCase() || "MANUAL",

        name: scraped.titulo,

        description: "",

        url: scraped.url,

        image: scraped.imagen,

        address: scraped.ubicacion,

        latitude: null,
        longitude: null,

        check_in: scraped.check_in,

        check_out: scraped.check_out,

        guests: scraped.viajeros ?? 1,

        price_per_night:
            scraped.noches && scraped.noches > 0
                ? scraped.precio / scraped.noches
                : scraped.precio,

        cleaning_fee: 0,

        service_fee: 0,

        taxes: 0,

        total_price: scraped.precio,

        currency: scraped.moneda,

        rating: scraped.puntuacion,

        reviews: Number(scraped.cantidad_resenas ?? 0),

        notes: "",

        status: "PLANNED",
    };
}