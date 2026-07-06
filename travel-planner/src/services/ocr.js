import { SCRAPER_API_URL } from "./api";

export async function importarTraslado(imagen) {

    const formData = new FormData();

    formData.append("imagen", imagen);

    const response = await fetch(
        API_URL + "/ocr/vuelo",
        {
            method: "POST",
            body: formData,
        }
    );

    if (!response.ok) {
        throw new Error("No se pudo importar el vuelo.");
    }

    return await response.json();
}