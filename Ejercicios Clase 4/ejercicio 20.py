suma = 0

while suma <= 100:
    numero = int(input("Ingresá un número para sumar: "))
    suma += numero
    print(f"Suma actual: {suma}")

print(f"¡Se te fué la mano! La suma final es {suma}, que supera el límite de 100.")