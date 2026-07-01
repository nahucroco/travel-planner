import { useNavigate } from "react-router-dom";
import Navbar from "../../components/Navbar/Navbar";
import Button from "../../components/Button/Button";
import "./NuevoViaje.css";

function NuevoViaje() {
    const navigate = useNavigate();

    return (
        <>
            <Navbar />
            <main className="nuevo-viaje">
                <div className="nuevo-viaje-header">
                    <p className="nuevo-viaje-eyebrow">Planificá tu aventura</p>
                    <h1 className="nuevo-viaje-title">Nuevo viaje</h1>
                </div>

                <div className="form-card">
                    <div className="form-field">
                        <label>Nombre del viaje</label>
                        <input className="form-input" placeholder="Ej: Verano en la Patagonia" />
                    </div>

                    <div className="form-field">
                        <label>Destino</label>
                        <input className="form-input" placeholder="Ciudad o región" />
                    </div>

                    <hr className="form-divider" />

                    <div className="form-row">
                        <div className="form-field">
                            <label>Fecha de salida</label>
                            <input className="form-input" type="date" />
                        </div>
                        <div className="form-field">
                            <label>Fecha de regreso</label>
                            <input className="form-input" type="date" />
                        </div>
                    </div>

                    <Button full onClick={() => navigate("/viajes/1")}>
                        Crear viaje →
                    </Button>
                </div>
            </main>
        </>
    );
}

export default NuevoViaje;
