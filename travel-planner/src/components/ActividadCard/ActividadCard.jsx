import Card from "../Card/Card";

function ActividadCard({

    actividad

}){

    return(

        <Card>

            <img
                src={actividad.imagen}
                alt={actividad.titulo}
            />

            <h3>

                {actividad.titulo}

            </h3>

            <p>

                {actividad.duracion}

            </p>

            <p>

                {actividad.precio_texto}

            </p>

        </Card>

    );

}

export default ActividadCard;