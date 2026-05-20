personas = {"Juan": 20, "Romina": 32, "Tamara": 25, "Melanie": 19}

with open("personas.txt", "w") as f:
    for nombre, edad in personas.items():
        f.write(f"{nombre.lower()}-{edad}\n")