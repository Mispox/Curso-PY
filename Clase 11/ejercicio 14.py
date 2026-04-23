fecha = input("Ingresá tu fecha de nacimiento (dd/mm/aaaa): ")
partes = fecha.split("/")
dia = partes[0]
mes = partes[1]
año = partes[2]

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")
# Funciona tanto con "1/3/2000" como con "01/03/2000"