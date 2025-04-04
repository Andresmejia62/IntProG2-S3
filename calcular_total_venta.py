#Calcular_total_venta
print("="*20)
print("Sistema de facturacion")
print("="*20)

cliente = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
descuento = float(input("Ingresa el descuento: "))
cantidad_producto = int(input("Ingrese la cantidad de productos: "))
precio_producto = float(input("Ingrese el precio del producto: "))
Subtotal= cantidad_producto * precio_producto


print("="*20)
print("Factura")
print("="*20)
print("Cliente: ", cliente)
print(f"Productos \t Cantidad \t Precio")
print(f"{producto}   \t {cantidad_producto}     \t {precio_producto}")
print("Total sin iva:", Subtotal)
iva = Subtotal * 0.15
print("Iva: ", iva)
total = Subtotal + iva - descuento
print("Descuento: ",descuento)
print("="*20)
print("Tu total a pagar es: ", total)
print("="*20)