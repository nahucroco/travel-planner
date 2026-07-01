import { useNavigate } from "react-router-dom";
import Navbar from "../../components/Navbar/Navbar";
import Button from "../../components/Button/Button";
import "./Home.css";

function Home() {
    const navigate = useNavigate();

    const viajes = [
        { id: 1, nombre: "Villa La Angostura", fechas: "4–9 ene 2027", emoji: "🏔️" },
        { id: 2, nombre: "Bariloche",           fechas: "15–20 jul 2027", emoji: "⛷️" },
    ];

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
                                        <div className="viaje-card-icon">{viaje.emoji}</div>
                                        <div className="viaje-card-info">
                                            <h3>{viaje.nombre}</h3>
                                            <p>📅 {viaje.fechas}</p>
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
