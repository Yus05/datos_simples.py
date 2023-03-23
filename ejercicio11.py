"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

 https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

 -> 4% de interes al ano.
 -> Mostrar cantidad de dinero de depositada, introducida por el usuario.
 -> Calcular y mostrar la cantidad de ahorros tras el 1er, 2do y 3er ano.
"""

interes = 4

dinero = int(input("Introduce la cantidad de dinero depositada: "))

calculo = int(((interes * dinero)/100))

primer_ano = str(calculo * 12)
segundo_ano = str(calculo * 24)
tercer_ano = str(calculo * 36)

print("Los intereses que ganaste el primer ano son: " + primer_ano)
print("Los intereses que ganaste el segundo ano son: " + segundo_ano)
print("Los intereses que ganaste el tercer ano son: " + tercer_ano)