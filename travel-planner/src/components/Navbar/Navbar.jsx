import { useNavigate, useLocation } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
    const navigate = useNavigate();
    const location = useLocation();
    const showBack = location.pathname !== "/";

    return (
        <header className="navbar">
            <div className="navbar-brand" onClick={() => navigate("/")} style={{ cursor: "pointer" }}>
                <div className="navbar-logo">✈️</div>
                <span className="navbar-name">Travel Planner</span>
            </div>
            {showBack && (
                <button className="navbar-back" onClick={() => navigate(-1)}>
                    ← Volver
                </button>
            )}
        </header>
    );
}

export default Navbar;
