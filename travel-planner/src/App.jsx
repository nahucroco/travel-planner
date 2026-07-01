import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home/Home";
import NuevoViaje from "./pages/NuevoViaje/NuevoViaje";
import Viaje from "./pages/Viaje/Viaje";

function App() {

    return (

        <Routes>

            <Route
                path="/"
                element={<Home />}
            />

            <Route
                path="/nuevo"
                element={<NuevoViaje />}
            />

            <Route
                path="/viajes/:id"
                element={<Viaje />}
            />

        </Routes>

    );

}

export default App;