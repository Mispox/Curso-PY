def pedir_numero(frase):
    while True:
        try:
            numero = float(input(frase))
            return numero
        except ValueError:
            print("Error: ingresá un número válido.")

# Uso:
edad = pedir_numero("Ingresá tu edad: ")
precio = pedir_numero("Ingresá el precio: ")
print(edad, precio)