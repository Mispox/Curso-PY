suma_total = 0
numero = int(input("Ingresá un número: "))

while numero != 0:
    suma_total += numero
    numero = int(input("Ingresá otro número: "))

print(f"La suma final es: {suma_total}")