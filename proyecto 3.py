# Alumnos: Lucas Mallofré, Milagros Loeda, Ivan Villalva
def validar_cantidad():
    while True:
        texto_ingresado = input("Ingresá la cantidad de juegos comprados: ")
        numeros_validos = 0 

        for caracter in texto_ingresado:
            if caracter in "0123456789":
                numeros_validos += 1

        if len(texto_ingresado) > 0 and numeros_validos == len(texto_ingresado):
            cantidad = int(texto_ingresado) 

            if cantidad > 0:
                break 
            else:
                print("Error: La cantidad debe ser mayor a cero.")
        else:
            print("Error: Debes ingresar unicamente numeros.")
    return cantidad 

def mostrar_socios(socios):
    print("\n--- LISTA DE SOCIOS ---")
    if len(socios) == 0:
        print("No hay socios registrados.")
    else:
        for socio in socios:
            print(f"Nombre: {socio} | juegos: {socios[socio]}")

def registro():
    socios = {}
    while True:
        try:
            print("Bienvenidx a la tienda de Juegos")
            print("\n--- MENU ---")
            print("1. Ingresar un nuevo socio")
            print("2. Ver lista de socios")
            print("3. Ver la cantidad de juegos de un socio")
            print("4. Salir")

            opcion = input("Elige una opcion (1-4): ")
            if opcion == '1':
                nombre = input("Ingresá el nombre del socio: ")
                cantidad = validar_cantidad()
                socios[nombre] = cantidad
                print("Socio registrado con exito.")
            elif opcion == '2':
                mostrar_socios(socios)
            elif opcion == '3':
                nombre = input("Ingresá el nombre del socio: ")
                if nombre in socios:
                    print(f"Cantidad de juegos: {socios[nombre]}")
                else:
                    print("El socio no existe")
            elif opcion == '4':
                print("Saliendo del programa")
                break
            else:
                print("Error: Opcion no valida")
        except Exception as e: 
            print(f"Error: {e}")

registro()