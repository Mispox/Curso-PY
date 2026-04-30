dato = input("Ingrese un numero: ")
while dato.isdecimal() == False:
    print("¡Error. Solo numeros!")
    dato = input("Ingrese un numero: ")

dato = int(dato)
print(type(dato), dato)