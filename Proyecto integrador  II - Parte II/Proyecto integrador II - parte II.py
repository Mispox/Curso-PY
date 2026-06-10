#Lucas Mallofré, Milagros Loeda, Bertho Berthelot
import time
import sqlite3

def conectar_db():
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS venta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            fecha TEXT,
            ComboS INTEGER,
            ComboD INTEGER,
            ComboT INTEGER,
            Flurby INTEGER,
            total REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encargado TEXT,
            fecha TEXT,
            evento TEXT,
            caja REAL
        )
    """)
    conn.commit()
    return conn

def validar_nombre(rol):
    while True:
        nombre = input(f"Ingresá el nombre del {rol}: ")
        if nombre == "" or nombre.isdigit():
            print("Error: el nombre debe contener al menos una letra")
        else:
            return nombre

def validar_cantidad(producto):
    while True:
        texto_ingresado = input(f"Ingrese cantidad {producto}: ")
        numeros_validos = 0

        for caracter in texto_ingresado:
            if caracter in "0123456789":
                numeros_validos += 1

        if len(texto_ingresado) > 0 and numeros_validos == len(texto_ingresado):
            cantidad = int(texto_ingresado)

            if cantidad >= 0:
                break
            else:
                print("Error: La cantidad no puede ser negativa.")
        else:
            print("Error: Debes ingresar unicamente numeros.")
    return cantidad

def bienvenida():
    print("Bienvenidx a la gestión de la caja de videojuegos")
    nombre = validar_nombre("encargado")
    return nombre

def menu(encargado):
    print(" Videojuegos IT ")
    print(f"Encargad@ -> {encargado}")
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")
    print("1 Ingresar nuevo pedido")
    print("2.Cambio turno")
    print("3.Apagar sistema")
    opcion = input("Elegí una opción: ")
    return opcion

def nuevo_pedido(conn):
    nombre_cliente = validar_nombre("cliente")
    cant_basico = validar_cantidad("Juego básico")
    cant_premium = validar_cantidad("Juego premium")
    cant_dlc = validar_cantidad("DLC")
    cant_pase = validar_cantidad("Pase de temporada")

    total = cant_basico * 15 + cant_premium * 25 + cant_dlc * 5 + cant_pase * 10
    print(f"Total ${total}")

    while True:
        pago = validar_cantidad("pago")
        if pago >= total:
            break
        else:
            print("Error: el pago no alcanza para cubrir el total.")

    vuelto = pago - total
    print(f"Vuelto ${vuelto}")

    while True:
        confirmacion = input("¿Confirma pedido? Y/N: ").upper()
        if confirmacion == "Y":
            fecha = time.ctime()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO venta (cliente, fecha, ComboS, ComboD, ComboT, Flurby, total) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (nombre_cliente, fecha, cant_basico, cant_premium, cant_dlc, cant_pase, total))
            conn.commit()
            print("Pedido confirmado")
            return total
        elif confirmacion == "N":
            print("Pedido cancelado")
            return 0
        else:
            print("Error: ingresá Y o N")

def registrar_entrada(encargado, conn):
    fecha = time.ctime()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
                   (encargado, fecha, "IN", 0))
    conn.commit()

def registrar_salida(encargado, total_caja, conn):
    fecha = time.ctime()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
                   (encargado, fecha, "OUT", total_caja))
    conn.commit()

def main():
    conn = conectar_db()
    encargado = bienvenida()
    registrar_entrada(encargado, conn)
    total_caja = 0
    while True:
        try:
            opcion = menu(encargado)
            if opcion == "1":
                total_caja += nuevo_pedido(conn)
            elif opcion == "2":
                registrar_salida(encargado, total_caja, conn)
                encargado = bienvenida()
                registrar_entrada(encargado, conn)
                total_caja = 0
            elif opcion == "3":
                registrar_salida(encargado, total_caja, conn)
                conn.close()
                print("Apagando sistema...")
                break
            else:
                print("Opción inválida")
        except Exception as e:
            print(f"Error: {e}")

main()