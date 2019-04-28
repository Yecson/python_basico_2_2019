
#Ejemplo 1
t=tuple(['mango','uvas','pera','manzana'])
print('la tupla es: ',t)

#Ejemplo 2: agregar un nuevo elemento

t1=tuple(['piña']) #forma 1

t3= t+('piña',) #forma 2

t2=t+t1

print(t2)
print(t3)

#3 Darlo los valores salteados

print(t[0],t[2])

t4=tuple(['mango','uvas','pera','manzana'])
t4[::2] #desde el primero al último en saltos de 2

t4[::-2] #desde el primero al último en saltos de 2 pero alrevez


