"""
	Practica 1: uso de funcion lambda
	autor: jecueva1997
"""
# Ingrese el numero a ser declarado
n = input("Ingrese el número: \n")
n = int(n)
# proceso para saber si es par o impar
par = lambda x: x%2 ==0
# presentacion del mensaje
print(par(n))

