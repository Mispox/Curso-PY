def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Eso no es un número.")

a = pedir_numero("Escribe un número: ")
b = pedir_numero("Escribe otro número: ")

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)

try:
    print("a / b:", a / b)
except ZeroDivisionError:
    print("No se puede dividir por cero")