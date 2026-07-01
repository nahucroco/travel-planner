import API_URL from "./api";

export async function importarItem(datos) {

    const response = await fetch(
        API_URL + "/scrape",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(datos),
        }
    );

    if (!response.ok) {
        throw new Error("No se pudo importar.");
    }

    return await response.json();

}