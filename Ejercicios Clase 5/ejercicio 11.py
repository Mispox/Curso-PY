deposito_inicial = float(input("Introduce la cantidad depositada en la cuenta: "))
interes_anual = 0.04

balance_ano_1 = deposito_inicial * (1 + interes_anual)
balance_ano_2 = balance_ano_1 * (1 + interes_anual)
balance_ano_3 = balance_ano_2 * (1 + interes_anual)

print(f"Cantidad de ahorros tras el primer año: {balance_ano_1:.2f}")
print(f"Cantidad de ahorros tras el segundo año: {balance_ano_2:.2f}")
print(f"Cantidad de ahorros tras el tercer año: {balance_ano_3:.2f}")