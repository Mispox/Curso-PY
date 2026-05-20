personas_recuperadas = {}

with open("personas.txt", "r") as f:
    for linea in f:
        linea = linea.strip()           
        partes = linea.split("-")       
        nombre = partes[0].capitalize() 
        edad = int(partes[1])          
        personas_recuperadas[nombre] = edad

print(personas_recuperadas)
