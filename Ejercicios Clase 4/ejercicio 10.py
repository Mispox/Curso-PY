cantidad_positivos = 0

for i in range(5):
    numero = int(input(f"Ingresá el número {i + 1}: "))
    if numero > 0:
        cantidad_positivos += 1

print(f"Ingresaste {cantidad_positivos} números positivos.")