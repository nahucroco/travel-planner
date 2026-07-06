import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { createTrip } from "../../api/trips";
import Navbar from "../../components/Navbar/Navbar";
import Button from "../../components/Button/Button";
import "./NuevoViaje.css";

function NuevoViaje() {
    const navigate = useNavigate();

    const [form, setForm] = useState({
        name: "",
        destination: "",
        start_date: "",
        end_date: "",
    });

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async () => {
        try {
            const trip = await createTrip(form);

            navigate(`/viajes/${trip.id}`);
        } catch (error) {
            console.error(error);
            alert("No se pudo crear el viaje.");
        }
    };

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
                        <input
                            name="name"
                            className="form-input"
                            placeholder="Ej: Verano en la Patagonia"
                            value={form.name}
                            onChange={handleChange}
                        />
                    </div>

                    <div className="form-field">
                        <label>Destino</label>
                        <input
                            name="destination"
                            className="form-input"
                            placeholder="Ciudad o región"
                            value={form.destination}
                            onChange={handleChange}
                        />
                    </div>

                    <hr className="form-divider" />

                    <div className="form-row">
                        <div className="form-field">
                            <label>Fecha de salida</label>
                            <input
                                name="start_date"
                                className="form-input"
                                type="date"
                                value={form.start_date}
                                onChange={handleChange}
                            />
                        </div>
                        <div className="form-field">
                            <label>Fecha de regreso</label>
                            <input
                                name="end_date"
                                className="form-input"
                                type="date"
                                value={form.end_date}
                                onChange={handleChange}
                            />
                        </div>
                    </div>

                    <Button full onClick={handleSubmit}>
                        Crear viaje →
                    </Button>
                </div>
            </main>
        </>
    );
}

export default NuevoViaje;
