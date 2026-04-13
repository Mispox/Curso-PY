def registro():
    socios = []

    while True:
        print ("Bienvenidx a la tienda de Juegos")
        print("\n--- MENU ---")
        print("1. Ingresar un nuevo socio")
        print("2. Ver lista de socios")
        print("3. Salir")
        
        opcion = input("Elige una opcion (1-3): ")

        if opcion == '1':
            nombre = input("Ingresá el nombre del socio: ")
            
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
            
            socios.append({"nombre": nombre, "cantidad": cantidad})
            print("Socio registrado con exito.")

        elif opcion == '2':
            print("\n--- LISTA DE SOCIOS ---")
            if len(socios) == 0:
                print("No hay socios registrados.")
            else:
                contador = 1
                for socio in socios:
                    print(f"{contador}. Nombre: {socio['nombre']} | juegos: {socio['cantidad']}")
                    contador += 1

        elif opcion == '3':
            print("Saliendo del programa")
            break

        else:
            print("Error: Opcion no valida")

registro()