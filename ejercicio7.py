"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

peso = int(input("Cual es tu peso en kilogramos? "))

estatura =float(input("Cual es tu estatura en metros? "))

formula = round((peso / (estatura)**2), 2)

formula = str(formula)

print("Tu indice de masa corporal es: " + formula)