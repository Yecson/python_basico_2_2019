# Crear un código que calcule las soluciones de la ecuación cuadrática de la forma ax2+bx+1=0
import math

a= float(input("favor ingresar el valor de 'a'"))
b= float(input("favor ingresar el valor de 'b'"))
c= float(input("favor ingresar el valor de 'c'"))

discriminante= b**2 -4*a*c

if discriminante < 0:
    raiz = math.sqrt(-discriminante)*complex(0,1)

else:
    raiz = math.sqrt(discriminante)

x1=(-b + raiz)/2*a
x2=(-b +- raiz)/2*a


print ("El valor de x1 es igual a",x1)
print ("El valor de x2 es igual a",x2)

# 2 a la 2 es igual a 2**2
#3 elevado a la 11 es igua a 2**11

#Otra solución


