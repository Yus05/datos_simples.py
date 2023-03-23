"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

 https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

-> barras_de_pan: 3.49 
-> descuento: 60%
-> Mostrar numero de barras vendidas que no son del dia, mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser del dia y el precio final. 
"""

BARRA_DE_PAN = 3.49

BARRA_DESCUENTO = 2.09

barras_vendidas = int(input("Introduce el numero de barras con descuento vendidas: "))

barras_sin_descuento = barras_vendidas * BARRA_DE_PAN
barras_con_descuento = barras_vendidas * BARRA_DESCUENTO

barras_sin_descuento = str(barras_sin_descuento)
barras_con_descuento = str(barras_con_descuento)

print("El precio habitual de una barra de pan es de: 3.49 pesos.")
print("El descuento por no ser pan del dia, es del 60%.")

print("El monto a pagar sin descuento es de: " + barras_sin_descuento)
print("El monto a pagar con descuento es de: " + barras_con_descuento)


#AHORA, VERIFICA EL CODIGO DE TUS EJERCICIOS CON LAS SOLUCIONES DE LA WEB. REPASA LOS CONCEPTOS DE LOS EJERCICIOS QUE SIGUEN Y DESPUES CONTINUA CON LOS EJERCICIOS. 