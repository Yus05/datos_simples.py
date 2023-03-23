"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

horas = int(input("Cuantas horas trabajaste en el dia? "))

coste = int(input("Cuanto te pagan por cada hora trabajada? "))

paga = str(horas * coste) 

print("Tu paga es de " + paga + " pesos")