"""
	Practica 3: uso de funcion lambda
	autor: jecueva1997
"""
# datos
lista = (10, 11)
# proceso de la suma en las posiciones en que se encuentra
suma = lambda x: x[0] + x[1]
# presentacion del mensaje
print(suma(lista))