capital = float(input("Capital en dólares: "))
tasa = float(input("Tasa de interés (%): "))
años = int(input("Número de años: "))

resultado = capital * (1 + tasa / 100) ** años
print(f"Capital final: {resultado:.2f} dólares")
# 10000, 4.5%, 20 años → 24117.14

