salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
impuesto_renta = salario_bruto * 0.10
seguro_social = salario_bruto * 0.05
fondo_pensiones = salario_bruto * 0.03
descuentos_totales = impuesto_renta + seguro_social + fondo_pensiones
salario_neto = salario_bruto - descuentos_totales
print(f"Salario Bruto: {salario_bruto:.2f} €")
print(f"Descuentos Totales: {descuentos_totales:.2f} €")
print(f"Salario Neto: {salario_neto:.2f} €")
