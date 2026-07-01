import Card from "../Card/Card";

import "./HospedajeCard.css";

function HospedajeCard({

    hospedaje

}){

    return(

        <Card>

            <img
                src={hospedaje.imagen}
                alt={hospedaje.titulo}
            />

            <h3>

                {hospedaje.titulo}

            </h3>

            <p>

                {hospedaje.plataforma}

            </p>

            <p>

                {hospedaje.precio_texto}

            </p>

        </Card>

    );

}

export default HospedajeCard;