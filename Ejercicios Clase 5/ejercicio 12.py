precio_barra = 3.49
descuento = 0.60 # 60% de descuento

barras_vendidas = int(input("Introduce el número de barras que no son del día vendidas: "))

coste_sin_descuento = barras_vendidas * precio_barra
total_descontado = coste_sin_descuento * descuento
coste_final = coste_sin_descuento - total_descontado

print(f"Precio habitual de una barra de pan fresca: ${precio_barra:.2f}")
print(f"Descuento total aplicado por no ser del día: ${total_descontado:.2f}")
print(f"Coste final total de la compra: ${coste_final:.2f}")