precio_original = float(input("Ingrese el precio original del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento aplicado: "))

descuento = (precio_original * porcentaje_descuento) / 100
precio_con_descuento = precio_original - descuento

porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))
iva_calculado = (precio_con_descuento * porcentaje_iva) / 100
precio_final = precio_con_descuento + iva_calculado

print(f"Precio Original: {precio_original:.2f} €")
print(f"Descuento Aplicado: {descuento:.2f} €")
print(f"Precio con Descuento: {precio_con_descuento:.2f} €")
print(f"IVA Calculado: {iva_calculado:.2f} €")
print(f"Precio Final: {precio_final:.2f} €")
