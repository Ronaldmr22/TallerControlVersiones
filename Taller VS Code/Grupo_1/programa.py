# Calcula el precio final de una compra.
precio = float(input("Precio original: "))
descuento = float(input("Descuento (%): "))

precio_final = precio - (precio * descuento)
print(f"Precio final: {precio_final:.2f}")
