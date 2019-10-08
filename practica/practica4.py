"""
	Practica 4: uso de funcion lambda
	autor: jecueva1997
"""
# datos
datos = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
# proceso para elevarlo al cubo
potencia = lambda x: x**3
# presentacion del mensaje
print(list(map(potencia, datos)))
