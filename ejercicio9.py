duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
comerciales_previos = float(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duracion_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))

total_comerciales_peliculas = cantidad_pausas * duracion_pausa
tiempo_total = duracion_pelicula + comerciales_previos + total_comerciales_peliculas

print(f"Duración de la película: {duracion_pelicula} minutos")
print(f"Duración de los comerciales previos: {comerciales_previos} minutos")
print(f"Total de comerciales durante la película: {total_comerciales_peliculas} minutos")
print(f"Tiempo total de la película con comerciales: {tiempo_total} minutos")
