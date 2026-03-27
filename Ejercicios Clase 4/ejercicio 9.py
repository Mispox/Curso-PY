numero_secreto = 7
intento = int(input("Adiviná el número secreto: "))

while intento != numero_secreto:
    intento = int(input("¡Incorrecto! Intentá de nuevo: "))

print("¡Adivinaste! El número secreto era el 7.")