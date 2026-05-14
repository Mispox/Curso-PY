def cubo(x):
    return x ** 3

def superior(funcion, lista):
    resultado = []
    for n in lista:
        resultado.append(funcion(n))
    return resultado

numeros = [2, 3, 4]
print(superior(cubo, numeros))
# out: [8, 27, 64]