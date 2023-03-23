"""
Escribir un programa que lea un entero positivo n introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.


 PASOS: 
 1- Solicitar numero entero.
 2- Crear formula que sume desde 1 hasta n.


"""

numero = int(input("Introduce un numero entero: "))

resultado = numero + 1 
resultado = int((resultado * numero) / 2) 

numero = str(numero)
resultado = str(resultado)

print("La sumatoria de los enteros que van desde 1 hasta " + numero + " es igual a: " + resultado)

# NOTA: VERIFICA LAS DUDAS QUE TIENES SOBRE LA EJECUCION DE LA FORMULA. LOS NOMBRE DE LAS VARIABLES Y COMPARA CON LA SOLUCION DE LA WEB.  


