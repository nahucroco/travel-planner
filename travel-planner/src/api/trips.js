const API_URL = "http://127.0.0.1:8000/api/trips/";

export async function getTrips() {
    const response = await fetch(API_URL);

    if (!response.ok) {
        throw new Error("No se pudieron obtener los viajes");
    }

    return response.json();
}

export async function createTrip(trip) {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(trip),
    });

    if (!response.ok) {
        throw new Error("Error al crear el viaje");
    }

    return response.json();
}