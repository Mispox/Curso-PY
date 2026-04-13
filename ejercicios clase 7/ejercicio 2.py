
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))

multiplos = []

for numero in range(inicio, fin + 1):
    if numero % 3 == 0 or numero % 5 == 0:
        multiplos.append(numero)

print(f"Los múltiplos de 3 y 5 en el rango de {inicio} a {fin} son:")
print(multiplos)