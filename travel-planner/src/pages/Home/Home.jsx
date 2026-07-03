import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { getTrips } from "../../api/trips";
import Navbar from "../../components/Navbar/Navbar";
import Button from "../../components/Button/Button";
import "./Home.css";

function Home() {
    const navigate = useNavigate();

    const [viajes, setViajes] = useState([]);

    useEffect(() => {
        async function cargarViajes() {
            try {
                const data = await getTrips();

                console.log("Viajes:", data);

                setViajes(data);
            } catch (error) {
                console.error("ERROR:", error);
            }
        }

        cargarViajes();
    }, []);
    
    return (
        <>
            <Navbar />
            <main className="home">
                <div className="home-header">
                    <p className="home-eyebrow">Bienvenido</p>
                    <h1 className="home-title">Mis viajes</h1>
                    <p className="home-subtitle">Planificá, organizá y disfrutá tus aventuras.</p>
                </div>

                <div className="home-actions">
                    <Button full onClick={() => navigate("/nuevo")}>
                        + Nuevo viaje
                    </Button>
                </div>

                {viajes.length > 0 ? (
                    <>
                        <p className="home-section-label">Próximos viajes</p>
                        <div className="viaje-list">
                            {viajes.map(viaje => (
                                <div
                                    key={viaje.id}
                                    className="viaje-card"
                                    onClick={() => navigate(`/viajes/${viaje.id}`)}
                                >
                                    <div className="viaje-card-body">
                                        <div className="viaje-card-icon">🧳</div>
                                        <div className="viaje-card-info">
                                            <h3>{viaje.name}</h3>
                                            <p>
                                                📅 {viaje.start_date} - {viaje.end_date}
                                            </p>
                                        </div>
                                    </div>
                                    <span className="viaje-card-arrow">›</span>
                                </div>
                            ))}
                        </div>
                    </>
                ) : (
                    <div className="home-empty">
                        <p style={{ fontSize: 32 }}>🗺️</p>
                        <p>Todavía no hay viajes. ¡Creá el primero!</p>
                    </div>
                )}
            </main>
        </>
    );
}

export default Home;
