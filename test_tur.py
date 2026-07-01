from scrapers.tur.scraper import obtener_actividad

actividad = obtener_actividad(
    "https://www.tur.com/es/san-martin-de-los-andes-160/caminata-bosque-encantado-con-raquetas-en-chapelco-4327?_gl=1*1ct7llh*_up*MQ..*_gs*MQ..&gclid=CjwKCAjw3ejRBhAdEiwADkqPn4drLoTyGPG05is-lqSRFr8j0gBr0TZp8F49-WtEpff24mxI6Tlo5BoCdK4QAvD_BwE&gbraid=0AAAAApKVqT3YWUQHn8LRMVcWgo1fP-KH-"   # la URL que estés usando
)

print()

print("Título:")
print(actividad.titulo)

print()

print("Imagen:")
print(actividad.imagen)

print()

print("Precio:")
print(actividad.precio)

print()

print("Moneda:")
print(actividad.moneda)

print()

print("Precio texto:")
print(actividad.precio_texto)

print()

print("Ubicación:")
print(actividad.ubicacion)

print()

print("Duración:")
print(actividad.duracion)

print()

print("Puntuación:")
print(actividad.puntuacion)

print()

print("Reseñas:")
print(actividad.cantidad_resenas)