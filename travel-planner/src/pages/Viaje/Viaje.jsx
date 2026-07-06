import { useState } from "react";
import { importarItem } from "../../services/scraper";
import Navbar from "../../components/Navbar/Navbar";
import Button from "../../components/Button/Button";
import ImportarModal from "../../components/ImportarModal/ImportarModal";
import TrasladoCard from "../../components/TrasladoCard/TrasladoCard";
import ConfirmDialog from "../../components/ConfirmDialog/ConfirmDialog";
import ImportarTrasladoModal from "../../components/ImportarTrasladoModal/ImportarTrasladoModal";
import { importarTraslado } from "../../services/ocr";
import "./Viaje.css";
import { Trash2 } from "lucide-react";
import { useParams } from "react-router-dom";
import { createAccommodation } from "../../services/accommodations";
import { mapScrapedAccommodation } from "../../mappers/accommodationMapper";


function ItemCard({ item, tipo, onDelete }) {
    return (
        <div className="item-card">
            <button
                className="item-card-delete"
                onClick={onDelete}
            >
                <Trash2 size={16} />
            </button>
            {item.imagen && (
                <img className="item-card-img" src={item.imagen} alt={item.titulo} />
            )}
            <div className="item-card-body">
                {item.plataforma && (
                    <span className="item-card-platform">{item.plataforma}</span>
                )}
                <h3 className="item-card-title">{item.titulo}</h3>
                {item.duracion && (
                    <span className="item-card-detail">⏱ {item.duracion}</span>
                )}
                {item.precio_texto && (
                    <span className="item-card-price">{item.precio_texto}</span>
                )}
            </div>
        </div>
    );
}

function Viaje() {
    const { id: tripId } = useParams();
    const [modalAbierto, setModalAbierto] = useState(false);
    const [modalTrasladoAbierto, setModalTrasladoAbierto] = useState(false);
    const [tipoImportacion, setTipoImportacion] = useState("");
    const [hospedajes, setHospedajes] = useState([]);
    const [actividades, setActividades] = useState([]);
    const [traslados, setTraslados] = useState([]);
    const [confirmDialog, setConfirmDialog] = useState({

        open: false,

        tipo: null,

        index: null,

    });

    const solicitarEliminar = (tipo, index) => {

        setConfirmDialog({
            open: true,
            tipo,
            index,
        });

    };

    const confirmarEliminar = () => {

        switch (confirmDialog.tipo) {

            case "hospedaje":
                setHospedajes(prev =>
                    prev.filter((_, i) => i !== confirmDialog.index)
                );
                break;

            case "actividad":
                setActividades(prev =>
                    prev.filter((_, i) => i !== confirmDialog.index)
                );
                break;

            case "traslado":
                setTraslados(prev =>
                    prev.filter((_, i) => i !== confirmDialog.index)
                );
                break;
        }

        setConfirmDialog({
            open: false,
            tipo: null,
            index: null,
        });

    };

    const abrirModal = (tipo) => {

        if (tipo === "traslado") {

            setModalTrasladoAbierto(true);
            return;

        }

        setTipoImportacion(tipo);
        setModalAbierto(true);

    };

    return (
        <>
            <Navbar />
            <main className="viaje">
                <div className="viaje-hero">
                    <p className="viaje-eyebrow">Tu próximo destino</p>
                    <h1 className="viaje-title">Villa La Angostura</h1>
                    <div className="viaje-meta">
                        <span className="viaje-meta-pill">📅 4–9 ene 2027</span>
                        <span className="viaje-meta-pill">👥 2 viajeros</span>
                        <span className="viaje-meta-pill">📍 Neuquén, Argentina</span>
                    </div>
                </div>

                {/* Hospedajes */}
                <div className="viaje-section">
                    <div className="viaje-section-header">
                        <h2 className="viaje-section-title">🏠 Hospedajes</h2>
                        <Button size="sm" onClick={() => abrirModal("hospedaje")}>
                            + Agregar
                        </Button>
                    </div>
                    <div className="item-grid">
                        {hospedajes.length === 0 ? (
                            <div className="section-empty">
                                <p style={{ fontSize: 28 }}>🛏️</p>
                                <p>Aún no hay hospedajes. Importá uno desde Airbnb o Booking.</p>
                            </div>
                        ) : (
                            hospedajes.map((h, index) => (

                                <ItemCard

                                    key={index}

                                    item={h}

                                    onDelete={() => solicitarEliminar("hospedaje", index)}

                                />

                            ))
                        )}
                    </div>
                </div>

                {/* Actividades */}
                <div className="viaje-section">
                    <div className="viaje-section-header">
                        <h2 className="viaje-section-title">🎿 Actividades</h2>
                        <Button size="sm" onClick={() => abrirModal("actividad")}>
                            + Agregar
                        </Button>
                    </div>
                    <div className="item-grid">
                        {actividades.length === 0 ? (
                            <div className="section-empty">
                                <p style={{ fontSize: 28 }}>🗺️</p>
                                <p>Sin actividades todavía. ¡Agregá algo que hacer!</p>
                            </div>
                        ) : (
                            actividades.map((a, index) => (

                                <ItemCard

                                    key={index}

                                    item={a}

                                    tipo="actividad"

                                    onDelete={() =>
                                        solicitarEliminar("actividad", index)
                                    }

                                />

                            ))
                        )}
                    </div>
                </div>

                {/* Traslados */}
                <div className="viaje-section">
                    <div className="viaje-section-header">
                        <h2 className="viaje-section-title">✈️ Traslados</h2>
                        <Button size="sm" onClick={() => abrirModal("traslado")}>
                            + Agregar
                        </Button>
                    </div>
                    <div className="item-grid">
                        {traslados.length === 0 ? (
                            <div className="section-empty">
                                <p style={{ fontSize: 28 }}>✈️</p>
                                <p>Todavía no agregaste ningún traslado.</p>
                            </div>
                        ) : (
                            traslados.map((t, index) => (

                                <TrasladoCard

                                    key={index}

                                    traslado={t}

                                    onDelete={() =>
                                        solicitarEliminar("traslado", index)
                                    }

                                />

                            ))
                        )}
                    </div>
                </div>

                <ImportarModal
                    open={modalAbierto}
                    tipo={tipoImportacion}
                    onClose={() => setModalAbierto(false)}
                    onImportar={async (url) => {
                        try {
                            const scraped = await importarItem({
                                url,
                                check_in: "2027-01-04",
                                check_out: "2027-01-09",
                                viajeros: 2,
                            });

                            const accommodation = mapScrapedAccommodation(
                                scraped,
                                tripId
                            );

                            console.log("Accommodation a guardar:", accommodation);

                            const savedAccommodation = await createAccommodation(
                                accommodation
                            );

                            if (tipoImportacion === "hospedaje") {
                                setHospedajes(prev => [...prev, savedAccommodation]);
                            }
                            setModalAbierto(false);
                        } catch (error) {
                            alert(error.message);
                        }
                    }}
                />
                <ImportarTrasladoModal

                    open={modalTrasladoAbierto}

                    onClose={() => setModalTrasladoAbierto(false)}

                    onImportar={async (imagen) => {

                        try {

                            const traslado = await importarTraslado(imagen);

                            setTraslados(prev => [

                                ...prev,

                                traslado

                            ]);

                            setModalTrasladoAbierto(false);

                        } catch (error) {

                            alert(error.message);

                        }

                    }}

                />
                <ConfirmDialog
                    open={confirmDialog.open}
                    title="Eliminar elemento"
                    message="¿Querés eliminar este elemento del viaje?"
                    onCancel={() =>
                        setConfirmDialog({
                            open: false,
                            tipo: null,
                            index: null,
                        })
                    }
                    onConfirm={confirmarEliminar}
                />
            </main>
        </>
    );
}

export default Viaje;
