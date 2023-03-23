"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""

numero_1 = int(input("Escribe un primer numero entero: "))

numero_2 = int(input("Escribe un segundo numero entero: "))

division = int(numero_1 / numero_2)

numero_1 = str(numero_1)

numero_2 = str(numero_2)

division = str(division)

print("La division entre " + numero_1 + " y " + numero_2 + " da un cociente: " + division + " y un resto: 0")

