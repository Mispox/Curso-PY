numero = input("Ingresá un número: ")
while not numero.isdecimal():
    print("Eso no es un número.")
    numero = input("Ingresá un número: ")
print("Número ingresado:", numero)