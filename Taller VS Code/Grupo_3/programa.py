# Verifica si hay unidades suficientes para una venta.
stock = 8
cantidad = int(input("Unidades solicitadas: "))

if cantidad >= stock:
    print("Venta autorizada")
else:
    print("No hay suficientes unidades")
