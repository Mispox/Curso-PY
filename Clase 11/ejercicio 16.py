nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))

total = precio * unidades
print(f"{nombre} {precio:09.2f} {unidades:03d} {total:011.2f}")