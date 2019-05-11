a=[1,3,5,8,7,9,2]
f=lambda x:x*10 #multiplica *10 all

#otra forma
[i*10 for in a]

[f(i) for in a]  #iterar por cada elemento
[(lamda x: x*10)(i) for i in a]


[(lamda x: x*10)(i) for i in a if i>5] # aplica la funcion a todo lo que sea mayor a 5 en a