import { useState } from "react";
import Modal from "../Modal/Modal";
import Button from "../Button/Button";

function ImportarTrasladoModal({

    open,
    onClose,
    onImportar,

}) {

    const [archivo, setArchivo] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleImportar = async () => {

        if (!archivo) return;

        setLoading(true);

        try {

            await onImportar(archivo);

            setArchivo(null);

        } finally {

            setLoading(false);

        }

    };

    return (

        <Modal
            open={open}
            onClose={onClose}
        >

            <div style={{ marginBottom: 20 }}>

                <p style={{
                    fontSize: 34,
                    marginBottom: 6
                }}>
                    ✈️
                </p>

                <h2 style={{
                    fontSize: 22,
                    marginBottom: 4
                }}>
                    Importar vuelo
                </h2>

                <p style={{
                    fontSize: 14,
                    color: "var(--slate)"
                }}>
                    Subí una captura o comprobante del vuelo y completaremos los datos automáticamente.
                </p>

            </div>

            <label
                style={{
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "center",
                    alignItems: "center",
                    gap: 12,
                    padding: "32px 20px",
                    border: "2px dashed var(--sand-mid)",
                    borderRadius: "var(--radius-md)",
                    background: "var(--sand)",
                    cursor: "pointer",
                    marginBottom: 20,
                }}
            >

                <span style={{ fontSize: 42 }}>

                    📄

                </span>

                <strong>

                    {archivo
                        ? archivo.name
                        : "Seleccionar imagen"}

                </strong>

                <span
                    style={{
                        fontSize: 13,
                        color: "var(--slate)",
                    }}
                >

                    PNG, JPG o JPEG

                </span>

                <input
                    type="file"
                    accept="image/png,image/jpeg,image/jpg"
                    style={{ display: "none" }}
                    onChange={(e) =>
                        setArchivo(e.target.files[0])
                    }
                />

            </label>

            <Button
                full
                disabled={!archivo || loading}
                onClick={handleImportar}
            >

                {loading
                    ? "Importando..."
                    : "Importar vuelo"}

            </Button>

        </Modal>

    );

}

export default ImportarTrasladoModal;