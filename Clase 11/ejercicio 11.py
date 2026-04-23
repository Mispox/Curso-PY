frase = input("Ingresá una frase: ")
vocal = input("Ingresá una vocal: ").lower()

resultado = ""
for letra in frase:
    if letra.lower() == vocal:
        resultado += letra.upper()
    else:
        resultado += letra

print(resultado)