"""
	Ejemplo 6: uso de funcion lambda
	autor: jecueva1997
"""

# utilizacion de map y listas con minimo
lista = [10, 2, 3, 5, 1]


funciones = lambda x: x + 100
print(min(list(map(funciones, lista))))
