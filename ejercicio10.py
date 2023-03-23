"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
PAYASO = 112

MUNECA = 75

payasos = int(input("Introduce el numero de payasos vendidos: "))

munecas = int(input("Introduce el numero de munecas vendidas: "))

peso_total = (payasos * PAYASO) + (munecas * MUNECA)

payasos = str(payasos)
munecas = str(munecas)
peso_total = str(peso_total)

print("El peso total del paquete a enviar es de: " + peso_total)
