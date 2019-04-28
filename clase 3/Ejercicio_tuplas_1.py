tupla=('a',1,2,None)
t=tuple([1,2,3,4])

print(t[0])

print(t[-1])

print(t[0:-1])

print(t[1:]) #si el final no está definido jala el extremo

print(t[:1]) #si el inicial no está definido jala el extremo

#Para el penúltimo hay dos opciones:
print(t[:-1]) #si el inicial no está definido jala el extremo
print(t[:3]) #si el inicial no está definido jala el extremo

#OPERACIONES CON TUPLAS:
t1=(1,2)+(6,7)
print(t1)