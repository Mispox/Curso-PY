inversion = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés porcentual anual? (ej. 5 para 5%): "))
anos = int(input("¿Número de años?: "))
capital_obtenido = inversion * (1 + interes / 100) ** anos
print(f"El capital obtenido en la inversión es: {capital_obtenido:.2f}")