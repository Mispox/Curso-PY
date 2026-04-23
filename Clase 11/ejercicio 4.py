palabra1 = input("Ingresá la primera palabra: ").lower()
palabra2 = input("Ingresá la segunda palabra: ").lower()

if palabra1[-3:] == palabra2[-3:]:
    print("¡Riman!")
elif palabra1[-2:] == palabra2[-2:]:
    print("Riman un poco.")
else:
    print("No riman.")