const API_URL = "http://127.0.0.1:8000/api/accommodations/";

export async function getAccommodationsByTrip(tripId) {

    const response = await fetch(
        `${API_URL}?trip=${tripId}`
    );

    if (!response.ok) {
        throw new Error("No se pudieron obtener los hospedajes.");
    }

    return response.json();

}

export async function createAccommodation(data) {

    console.log("Enviando:", data);

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    const body = await response.json();

    console.log("Status:", response.status);
    console.log("Respuesta:", body);

    if (!response.ok) {
        throw new Error(JSON.stringify(body));
    }

    return body;
}

export async function deleteAccommodation(id) {

    const response = await fetch(
        `${API_URL}${id}/`,
        {
            method: "DELETE",
        }
    );

    if (!response.ok) {
        throw new Error("No se pudo eliminar.");
    }

}