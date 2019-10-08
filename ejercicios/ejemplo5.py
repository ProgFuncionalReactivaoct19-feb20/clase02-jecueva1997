"""
	Ejemplo 5: uso de funcion lambda
	autor: jecueva1997
"""
# se encuentran meses y estatura de una persona
# utilizacion de map para que devuelva de mejor la manera la visualizacion 
datos = (
		(100, 170),
		(200, 180),
		)
anios = lambda x: x[0]
estatura = lambda x: x[1]

funciones = lambda x: (anios(x)/12.0, estatura(x)/100)

print(list(map(funciones, datos)))
