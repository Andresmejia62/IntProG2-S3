#Conversión de unidades de tiempo
print("Bienvenido a tu conversora de unidades de tiempo")
segundos_totales = int(input("Ingrese la cantidad total de segundos: "))

horas = segundos_totales // 3600
segundos_restantes = segundos_totales - (horas * 3600)

minutos = segundos_restantes // 60
segundos = segundos_restantes - (minutos * 60)

print(f"Tiempo: {horas} horas, {minutos} minutos, {segundos} segundos")
