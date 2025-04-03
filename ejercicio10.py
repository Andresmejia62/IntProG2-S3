duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
comerciales_previos = float(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duracion_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))

total_comerciales_peliculas = cantidad_pausas * duracion_pausa
tiempo_con_comerciales_previos = duracion_pelicula + comerciales_previos
duracion_total = tiempo_con_comerciales_previos + total_comerciales_peliculas

print(f"Duración original de la película: {duracion_pelicula} minutos")
print(f"Duración de los comerciales totales: {comerciales_previos + total_comerciales_peliculas} minutos")
print(f"Tiempo total de la proyección: {duracion_total} minutos")
