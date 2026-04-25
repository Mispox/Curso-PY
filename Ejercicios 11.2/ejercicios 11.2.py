# Ejercicio 1 - Máximo de dos números
def max(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "Son iguales"

# Ejercicio 2 - Máximo de tres números
def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    else:
        return "Son iguales"

# Ejercicio 3 - Longitud de lista o cadena
def largo_cadena(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

# Ejercicio 4 - Es vocal
def es_vocal(x):
    if x.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

# Ejercicio 5 - Suma y multiplicación de lista
def suma(lista):
    total = 0
    for i in lista:
        total += i
    return total

def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

# Ejercicio 6 - Invertir cadena
def inversa(cadena):
    invertida = ""
    for i in cadena:
        invertida = i + invertida
    return invertida

# Ejercicio 7 - Es palíndromo
def es_palindromo(cadena):
    if cadena == inversa(cadena):
        return True
    else:
        return False

# Ejercicio 8 - Superposición de listas
def superposicion(lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

# Ejercicio 9 - Generar n caracteres
def generar_n_caracteres(n, caracter):
    return n * caracter

# Ejercicio 10 - Histograma
def procedimiento(lista):
    for i in lista:
        print(i * "*")


# --- PRUEBAS ---
print(max(3, 7))                          # 7
print(max_de_tres(5, 2, 8))              # 8
print(largo_cadena([1, 2, 3, 4]))        # 4
print(largo_cadena("hola"))              # 4
print(es_vocal("a"))                     # True
print(es_vocal("b"))                     # False
print(suma([1, 2, 3, 4]))               # 10
print(multip([1, 2, 3, 4]))             # 24
print(inversa("estoy probando"))         # odnaborp yotse
print(es_palindromo("radar"))           # True
print(es_palindromo("python"))          # False
print(superposicion([1,2,3], [4,2,6]))  # True
print(superposicion([1,2,3], [4,5,6]))  # False
print(generar_n_caracteres(5, "x"))     # xxxxx
procedimiento([4, 9, 7])
# ****
# *********
# *******