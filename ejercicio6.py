#Cálculo del índice de masa corporal
print("Bienvenido a tu calculadora de índice de masa corporal")
peso_kg = float(input("Ingresa tu peso en kg "))
altura_m = float(input("Ingresa tu altura en metros"))
altura_2 = altura_m * altura_m
IMC = peso_kg / altura_2
IMC_red = IMC * 100 
IMC_red = round(IMC / 100)
print(f"Peso: {peso_kg} kg")
print(f"Altura: {altura_m} m")
print(f"IMC: {IMC_red}")
if IMC < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= IMC < 24.9:
    clasificacion = "Peso normal"
elif 25 <= IMC < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Clasificación: {clasificacion}")