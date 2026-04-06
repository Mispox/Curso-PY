peso_payaso = 112
peso_muñeca = 75

payasos_vendidos = int(input("Introduce el número de payasos vendidos: "))
munecas_vendidas = int(input("Introduce el número de muñecas vendidas: "))

peso_total = (payasos_vendidos * peso_payaso) + (munecas_vendidas * peso_muñeca)
print(f"El peso total del paquete a enviar es de {peso_total} gramos.")