#5 Utilizando pasos 1 , 2 y 4 para sacar de la lista las verduras.
# Qué le pasa a la lista de compras si se quitan todas las verduras

#1 Crear listas de las categorías
#2 Crear lista de compras general

verduras= ['tomates','papas','cebolla','ajos']
frutas= ['piña','naranja','sandía']
carnes= ['mortadela','pollo','costilla de cerdo']
limpieza= ['jabón','cloro','shampoo']
lista_de_compras= [verduras,frutas,carnes,limpieza]

#4 agregar a la lista de verduras 'chile' y a la lista de frutas 'mango' e investigar el efecto en la lista principal

frutas.append('mango')
verduras.append('chile')

#verduras=[] # no borra la lista si ésta esta después
#verduras.clear()  # si funcion para borar la lista declarada anteriormente
del verduras [:] # si funcion para borar la variable declarada anteriormente

print(lista_de_compras)


