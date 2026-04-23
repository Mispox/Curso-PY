telefono = input("Ingresá el teléfono (ej: +34-913724710-56): ")
partes = telefono.split("-")
print(partes[1])   # Solo el número central
