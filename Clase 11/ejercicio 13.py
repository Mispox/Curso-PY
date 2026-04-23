precio = input("Ingresá el precio (ej: 3.75): ")
partes = precio.split(".")
euros = partes[0]
centimos = partes[1] if len(partes) > 1 else "00"

print(f"Euros: {euros}")
print(f"Céntimos: {centimos}")

