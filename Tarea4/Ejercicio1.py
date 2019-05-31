hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]
def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

# la tabla resultante luego de aplicar transpuesta
hoja_calculo_T = transpuesta(hoja_calculo)

# Permite extender la lista en elementos
def extender_lista(l):
    m = []
    for i in l:
        if isinstance(i, list): # verifica si es una lista
            m.extend(i)  # en caso de ser una sublista
        else:
            m.append(i)  # en caso de que sean elementos simples
    return m

#otra forma de extender lista de sublistas
extender_lista_version2 = lambda l : [j for i in l for j in i]

from functools import reduce

tool_box= {
    'suma': sum,
    'multiplicacion' : lambda z :reduce(lambda x,y:x*y, z, 1),
    'promedio' : lambda x: sum(x) / len(x)

}

lista_extendida = extender_lista(hoja_calculo_T[1:])

multiplicacion = tool_box['multiplicacion'](lista_extendida)
suma = tool_box['suma'](lista_extendida)
promedio = tool_box['promedio'](lista_extendida)

print('Usando todos los números')
print('suma=',suma)
print('multiplicacion=', multiplicacion)
print('promedio=', promedio)

#Promedio > saldo (ahorro) debito 1
promedio = tool_box['promedio'](hoja_calculo_T[1])
print('promedio de los saldos=', promedio)

#La suma > deuda 3
suma = tool_box['suma'](hoja_calculo_T[3])
print('suma de las deudas=', suma)

#La multiplicación > credito 2
multiplicacion = tool_box['multiplicacion'](hoja_calculo_T[2])
print('multiplicacion de los creditos=', multiplicacion)

# calculo del impuesto

calculo_impuesto =lambda l :[i*1.2 for i in l]
print('Sin impuesto')
print(hoja_calculo_T)
hoja_calculo_T[2] = calculo_impuesto(hoja_calculo_T[2])

print('Con impuesto')
print(hoja_calculo_T)
pass