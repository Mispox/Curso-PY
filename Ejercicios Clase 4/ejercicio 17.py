contraseña_correcta = "python123"
intento = input("Ingresá la contraseña: ")

while intento != contraseña_correcta:
    intento = input("Contraseña incorrecta. Intentá de nuevo: ")

print("¡Acceso concedido!")