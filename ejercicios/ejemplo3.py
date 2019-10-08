"""
	Ejemplo 3: uso de funcion lambda
	autor: jecueva1997
"""

# cada elemento de datos, tiene (edad y estaura)
# duplas
datos = ((30, 1.79)), ((25, 1.60)), ((35, 1.68))
dato = lambda x: x[2]
print(dato(datos))