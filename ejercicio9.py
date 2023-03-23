"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.


"""

inversion = int(input("Introduce el monto de tu inversion: "))

interes = int(input("Introduce el interes anual: "))

anos = int(input("Introduce la cantidad de anos que durara la inversion: "))

formula = int(((interes * inversion)/100) * (anos * 12))

formula = str(formula)

print("El capital obtenido de tu inversion es de: " + formula + "$")

