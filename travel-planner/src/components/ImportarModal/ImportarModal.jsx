import { useState } from "react";
import Modal from "../Modal/Modal";
import Button from "../Button/Button";

const config = {
    hospedaje: {
        title: "Importar hospedaje",
        icon: "🏠",
        placeholder: "https://www.airbnb.com.ar/rooms/...",
        hint: "Pegá el link de Airbnb, Booking o cualquier alojamiento.",
    },
    actividad: {
        title: "Importar actividad",
        icon: "🎿",
        placeholder: "https://www.civitatis.com/...",
        hint: "Pegá el link de Civitatis, GetYourGuide u otro sitio.",
    },
};

function ImportarModal({ open, tipo, onClose, onImportar }) {
    const [url, setUrl] = useState("");
    const [loading, setLoading] = useState(false);
    const info = config[tipo] || config.hospedaje;

    const handleImportar = async () => {
        if (!url.trim()) return;
        setLoading(true);
        try {
            await onImportar(url);
            setUrl("");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Modal open={open} onClose={onClose}>
            <div style={{ marginBottom: 20 }}>
                <p style={{ fontSize: 28, marginBottom: 6 }}>{info.icon}</p>
                <h2 style={{ fontSize: 22, marginBottom: 4 }}>{info.title}</h2>
                <p style={{ fontSize: 14, color: 'var(--slate)' }}>{info.hint}</p>
            </div>

            <div style={{ marginBottom: 16 }}>
                <input
                    style={{
                        width: '100%',
                        padding: '13px 15px',
                        borderRadius: 'var(--radius-sm)',
                        border: '1.5px solid var(--sand-mid)',
                        background: 'var(--sand)',
                        fontSize: 14,
                        outline: 'none',
                        color: 'var(--ink)',
                        fontFamily: 'Inter, sans-serif',
                        boxSizing: 'border-box',
                    }}
                    value={url}
                    onChange={e => setUrl(e.target.value)}
                    placeholder={info.placeholder}
                    onKeyDown={e => e.key === 'Enter' && handleImportar()}
                    autoFocus
                />
            </div>

            <Button
                full
                onClick={handleImportar}
                disabled={loading || !url.trim()}
            >
                {loading ? "Importando…" : "Importar"}
            </Button>
        </Modal>
    );
}

export default ImportarModal;
