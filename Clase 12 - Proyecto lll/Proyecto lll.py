# Alumnos: Lucas Mallofré, Milagros Loeda, Ivan Villalva
def validar_nombre():
    while True:
        nombre = input("Ingresá el nombre del socio: ")
        if nombre == "":
            print("Error: el nombre no puede estar vacío")
        else:
            return nombre

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

def buscar_socio(socios):
    nombre = validar_nombre()
    if nombre in socios:
        print(f"Cantidad de juegos: {socios[nombre]}")
    else:
        print("El socio no existe")

def agregar_socio(socios): 
    nombre = validar_nombre()
    cantidad = validar_cantidad() 
    socios[nombre] = cantidad 
    print("Socio registrado con exito.")
def jugador_mas_compras(socios):
    if len(socios) == 0:
        print("No hay socios registrados.")
    else:
        jugador_max = max(socios, key=socios.get)
        print(f"El jugador con más compras es: {jugador_max} con {socios[jugador_max]} juegos")
def total_juegos(socios):
    if len(socios) == 0:
        print("No hay socios registrados.")
    else:
        total = 0
        for socio in socios:
            total += socios[socio]
        print(f"Total de juegos vendidos: {total}")
def eliminar_socio(socios):
    nombre = validar_nombre()
    if nombre in socios:
        del socios[nombre]
        print(f"El socio {nombre} fue eliminado.")
    else:
        print("El socio no existe")

def registro():
    socios = {}
    while True:
        try:
            print("Bienvenidx a la tienda de Juegos")
            print("\n--- MENU ---")
            print("1. Ingresar un nuevo socio")
            print("2. Ver lista de socios")
            print("3. Ver la cantidad de juegos de un socio")
            print("4. Jugador con más compras")
            print("5.Total juegos vendidos")
            print("6.Eliminar jugador")
            print("7.Salir")

            opcion = input("Elige una opcion (1-7): ")
            if opcion == '1':
                agregar_socio(socios)
            elif opcion == '2':
                mostrar_socios(socios)
            elif opcion == '3':
                buscar_socio(socios)
            elif opcion == '4':
                jugador_mas_compras(socios)
            elif opcion == '5': 
                total_juegos(socios)
            elif opcion == '6':
                eliminar_socio(socios)
            elif opcion == '7':
                print("Saliendo del programa")
                break
            else:
                print("Error: Opcion no valida")
        except Exception as e: 
               print(f"Error: {e}")

registro()