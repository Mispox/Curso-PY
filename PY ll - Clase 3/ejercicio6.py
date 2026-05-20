import time

def registrar(nombre, tipo):
    fecha = time.asctime()
    with open("registro.txt", "a") as f:
        f.write(f"{fecha} - {nombre} - {tipo}\n")

while True:
    print("\n1 - Ingreso de empleado")
    print("2 - Egreso de empleado")
    print("3 - Salir del sistema")
    opcion = input(">>> ")

    match opcion:
        case "1":
            nombre = input("Nombre del empleado: ")
            registrar(nombre, "Ingreso")
        case "2":
            nombre = input("Nombre del empleado: ")
            registrar(nombre, "Egreso")
        case "3":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida")