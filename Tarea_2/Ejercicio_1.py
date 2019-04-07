#Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista
mis_valores = [5, 6, 10, 13, 3, 4]

#Funcion que recibe un arreglo de valores y retorna el promedio de ellos
def promedio(mis_valores):
	sumaParcial=0
	for valor in mis_valores:
		sumaParcial+=valor
	#La funcion len calcula la longitud del arreglo, que va a ser el valor por el cual habra que dividir para obtener un promedio
	cantidadValores = len(mis_valores)
	#En el calculo del promedio, le digo a Python que inteprete a cantidadValores como decimal y no como entero, para que me devuelva un resultado decimal. Esto lo hago poniendo la funcion float()
	return sumaParcial/float(cantidadValores)

#Llamamos a la funcion de impresion por consola (print) para que muestre el resultado de llamar a la funcion "promedio" con el arreglo "valores" como argumento
print(round(promedio(mis_valores),2))