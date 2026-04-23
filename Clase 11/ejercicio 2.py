personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]

conteo = {}
for persona in personas:
    if persona in conteo:
        conteo[persona] += 1
    else:
        conteo[persona] = 1

print(conteo)
# {'Susana': 3, 'Tamara': 1, 'Ana': 2, 'Tomas': 1}