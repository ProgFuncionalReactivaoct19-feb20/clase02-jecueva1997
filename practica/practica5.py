"""
	Practica 5: uso de funcion lambda
	autor: jecueva1997
"""
# importacion de las operaciones a utilizar
import math
# datos del listado de duplas
datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]
# posiciones 
posicion_1 = lambda x: x[0]
posision_2 = lambda x: x[1]
# proceso para sacar la raiz y la potencia 
funcion = lambda x: (math.sqrt(posicion_1(x)), posision_2(x)**2)
# imprecion del mensaje
print(list(map(funcion, datos)))