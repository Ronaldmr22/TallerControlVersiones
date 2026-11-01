def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

print("=== CALCULADORA ===")
print("1. Sumar")
print("2. Restar")

opcion = input("Seleccione una opción: ")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if opcion == "1":
    print("Resultado:", sumar(a, b))
elif opcion == "2":
    print("Resultado:", restar(a, b))
else:
    print("Opción inválida")