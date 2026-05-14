paises = {
    "ar": "Argentina",
    "es": "España",
    "us": "Estados Unidos",
    "fr": "Francia"
}

while True:
    codigo = input("Ingresá el código de un país (o 'salir'): ")
    if codigo == "salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("Ese código no existe. Probá de nuevo.")