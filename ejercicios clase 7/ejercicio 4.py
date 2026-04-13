cantidad = int(input("¿Cuántos nombres desea ingresar?: "))
nombres = []

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres.append(nombre)

print("\n--------------------")
nombre_buscado = input("Ingrese el nombre que desea buscar en la lista: ")

contador = 0

for nombre in nombres:
    
    if nombre.lower() == nombre_buscado.lower(): 
        contador += 1

print(f"El nombre '{nombre_buscado}' aparece {contador} vez/veces en la lista.")