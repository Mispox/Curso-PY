n = int(input("¿Cuántos números de Fibonacci necesitás?: "))
a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b