#Cálculo del tiempo total de un viaje con escalas 
Primer_tramo = int(input("Ingresa la duración del primer tramo del vuelo:"))
Primera_esc = int(input("Ingresar la duración de la primera escala: "))
Segundo_tramo = int(input("Ingresa la duración del segundo tramo del vuelo:"))
Segunda_esc = int(input("Ingresar la duración de la segunda escala: "))
Tercer_tramo = int(input("Ingresa la duración del tercer tramo del vuelo:"))
Resultado = Primer_tramo + Primera_esc
Resultado = Resultado + Segundo_tramo
Resultado = Resultado + Segunda_esc
Resultado = Resultado + Tercer_tramo
print ("El tiempo total de tu viaje es de:", Resultado)