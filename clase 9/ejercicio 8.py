personas = {}

while True:
    print("\n1. Agregar\n2. Más chico\n3. Más grande\n4. Salir")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        personas[nombre] = edad

    elif opcion == "2":
        if personas:
            mas_chico = min(personas, key=personas.get)
            print("El más chico es:", mas_chico)

    elif opcion == "3":
        if personas:
            mas_grande = max(personas, key=personas.get)
            print("El más grande es:", mas_grande)

    elif opcion == "4":
        break