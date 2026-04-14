def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    print(f"{n}! =", resultado)

factorial(6)