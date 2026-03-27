palabra = input("Ingresá una palabra: ").lower()
cantidad_vocales = 0

vocales = "aeiou"

for letra in palabra:
    if letra in vocales:
        cantidad_vocales += 1

print(f"La palabra tiene {cantidad_vocales} vocales.")