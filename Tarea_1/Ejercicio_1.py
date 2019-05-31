#Escribir un código en Python que imprima en pantalla lo siguiente:
# * 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14

from math import pi
a= pi %1
b=int(pi)
c=b+a

print("El numero pi completo es igual a: ",c)

str = '* '
print(str[:1]*1,round(c,7),str[:1]*2,round(c,5),str[:1]*3,round(c,4),str[:1]*4,round(c,3),str[:1]*5,round(c,2))


