const SCRAPER_URL = "http://127.0.0.1:8001";

export async function importarItem(datos) {

    const response = await fetch(
        `${SCRAPER_URL}/scrape`,
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

    return response.json();
}