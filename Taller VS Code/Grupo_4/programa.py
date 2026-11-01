# Busca un nombre en la lista de participantes.
participantes = ["Ana", "Luis", "Marta", "Pedro"]
nombre = input("Nombre a buscar: ").strip()

if nombre.lower() in participantes:
    print("Participante encontrado")
else:
    print("Participante no encontrado")
