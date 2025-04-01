base_rect = float(input("Introduce la base del rectángulo: "))
alt_rect = float(input("Introduce la altura del rectángulo: "))
area_rect = base_rect * alt_rect
perimetro_rect = (2 * base_rect) + (2 * alt_rect)

print(f"El área del rectángulo es {area_rect:.2f}")
print(f"El perímetro del rectángulo es {perimetro_rect:.2f}")
