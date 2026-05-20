def mayusculas(texto):
    separo = texto.split()
    return f"{separo[0].capitalize()} {separo[1].capitalize()}"

def aplicar(funcion, lista):
    nueva = []
    for n in lista:
        nueva.append(funcion(n))
    return nueva

personas = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]
print(aplicar(mayusculas, personas))
