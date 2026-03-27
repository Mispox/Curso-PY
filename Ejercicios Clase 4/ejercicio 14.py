numero = int(input("Ingresá un número para ver sus divisores: "))
print(f"Los divisores de {numero} son:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)