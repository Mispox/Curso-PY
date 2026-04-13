cantidad = int(input("¿Cuántos nombres desea ingresar?: "))
nombres = []

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres.append(nombre)

print("\n--- Lista creada ---")
for nombre in nombres:
    print(nombre)