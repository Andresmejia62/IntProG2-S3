temp_fah=float(input("Ingresa la temperatura en Fahrenheit: "))
temp_cel = temp_fah - 32
temp_cel = temp_cel * 5
temp_cel = temp_cel / 9
temp_kel = temp_cel + 273.15
print(f"La temperatura en Celsius es  { temp_cel:.2f}")
print(f"La temperatura en Kelvin es  { temp_kel:.2f}")