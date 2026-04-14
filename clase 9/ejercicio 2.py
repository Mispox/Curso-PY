import random

while True:
    print("\n1. Tirar dado\n2. Salir")
    opcion = input("Elegí una opción: ")
    if opcion == "1":
        print("Salió:", random.randint(1, 6))
    elif opcion == "2":
        break