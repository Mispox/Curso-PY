def pedir_entero():
    dato = input("Ingresá un número entero: ")
    while not dato.isdecimal():
        print("No es un entero válido.")
        dato = input("Ingresá un número entero: ")
    return int(dato)

numero = pedir_entero()
print("Número convertido:", numero)