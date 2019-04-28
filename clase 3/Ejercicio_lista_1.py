#1 Crear listas de las categorías
#2 Crear lista de compras general

verduras= ['tomates','papas','cebolla','ajos']
frutas= ['piña','naranja','sandía']
carnes= ['mortadela','pollo','costilla de cerdo']
limpieza= ['jabón','cloro','shampoo']
lista_de_compras= [verduras,frutas,carnes,limpieza]

#3 cuántos artículos voy a comprar

mi_lista =[]
for categoria in lista_de_compras:
    mi_lista.extend(categoria)
    print(mi_lista)
print(len(mi_lista))

#4 agregar a la lista de verduras 'chile' y a la lista de frutas 'mango' e investigar el efecto en la lista principal

frutas.append('mango')
verduras.append('chile')
print(lista_de_compras)


cantidad = 0
for categoria in lista_de_compras:
    cantidad += len(categoria)
print(cantidad)