import Card from "../Card/Card";
import "./TrasladoCard.css";
import { Trash2 } from "lucide-react";

function TrasladoCard({ traslado, onDelete }) {

    return (

        <Card>
            <button
                className="item-card-delete"
                onClick={onDelete}
            >
                <Trash2 size={16} />
            </button>

            <span className="traslado-platform">

                {traslado.plataforma}

            </span>

            {traslado.proveedor && (

                <h3 className="traslado-provider">

                    ✈️ {traslado.proveedor}

                </h3>

            )}

            <div className="traslado-route">

                <div>

                    <span className="traslado-code">

                        {traslado.origen}

                    </span>

                    <span className="traslado-label">

                        Origen

                    </span>

                </div>

                <div className="traslado-arrow">

                    ─────►

                </div>

                <div>

                    <span className="traslado-code">

                        {traslado.destino}

                    </span>

                    <span className="traslado-label">

                        Destino

                    </span>

                </div>

            </div>

            <div className="traslado-info">

                <div>

                    <span>📅</span>

                    <span>{traslado.fecha_salida}</span>

                </div>

                <div>

                    <span>🕒</span>

                    <span>

                        {traslado.hora_salida}

                        {" → "}

                        {traslado.hora_llegada}

                    </span>

                </div>

                {traslado.duracion && (

                    <div>

                        <span>⏱</span>

                        <span>{traslado.duracion}</span>

                    </div>

                )}

                {traslado.escalas !== null &&
                    traslado.escalas !== undefined && (

                        <div>

                            <span>🛑</span>

                            <span>

                                {traslado.escalas === 0
                                    ? "Directo"
                                    : `${traslado.escalas} escala${traslado.escalas > 1 ? "s" : ""}`}

                            </span>

                        </div>

                    )}

            </div>

            {traslado.precio_texto && (

                <div className="traslado-price">

                    {traslado.precio_texto}

                </div>

            )}

        </Card>

    );

}

export default TrasladoCard;