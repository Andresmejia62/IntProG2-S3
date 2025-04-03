dolares = float(input("Ingrese la cantidad en dólares: "))

tasa_euros = float(input("Ingrese la tasa de cambio de dólares a euros: "))
tasa_libras = float(input("Ingrese la tasa de cambio de dólares a libras: "))
tasa_yenes = float(input("Ingrese la tasa de cambio de dólares a yenes: "))

cantidad_euros = dolares * tasa_euros
cantidad_libras = dolares * tasa_libras
cantidad_yenes = dolares * tasa_yenes

print(f"Cantidad en dólares: {dolares:.2f} USD")
print(f"Cantidad en euros: {cantidad_euros:.2f} EUR")
print(f"Cantidad en libras: {cantidad_libras:.2f} GBP")
print(f"Cantidad en yenes: {cantidad_yenes:.2f} JPY")
