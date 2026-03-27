numero = int(input("Ingresá un número: "))
mayor = numero

while numero != 0:
    if numero > mayor:
        mayor = numero
    numero = int(input("Ingresá otro número: "))

print(f"El número mayor ingresado fue: {mayor}")