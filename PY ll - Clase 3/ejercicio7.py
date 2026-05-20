import time

def registrar(nombre, tipo):
    fecha = time.asctime()
    with open("registro.txt", "a") as f:
        f.write(f"{fecha} - {nombre} - {tipo}\n")

def ver_ultimos():
    with open("registro.txt", "r") as f:
        lineas = f.readlines()
    if not lineas:
        print("No hay registros")
    else:
        ultimos = lineas[-5:]   # toma los últimos 5 (o menos si hay menos)
        for linea in ultimos:
            print(linea.strip())

while True:
    print("\n1 - Ingreso de empleado")
    print("2 - Egreso de empleado")
    print("3 - Mostrar los últimos 5 registros")
    print("4 - Salir del sistema")
    opcion = input(">>> ")

    match opcion:
        case "1":
            nombre = input("Nombre del empleado: ")
            registrar(nombre, "Ingreso")
        case "2":
            nombre = input("Nombre del empleado: ")
            registrar(nombre, "Egreso")
        case "3":
            ver_ultimos()
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida")