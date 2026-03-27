suma_total = 0

for i in range(5):
    numero = int(input(f"Ingresá el número {i + 1}: "))
    suma_total += numero

promedio = suma_total / 5
print(f"El promedio es: {promedio}")