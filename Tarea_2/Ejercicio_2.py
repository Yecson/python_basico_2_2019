
Grupo_1 = [177,145,167,190,140,150,180,130]
Grupo_2 = [165,176,145,189,170,189,159,190]
Grupo_3 = [145,136,178,200,123,145,145,134]
Grupo_4 = [201,110,187,175,156,165,156,135]

a= max(Grupo_1)
b= max(Grupo_2)
c= max(Grupo_3)
d= max(Grupo_4)

Grupo_maximos = [a,b,c,d]

e= max(Grupo_maximos)

if e == a:
    print("El valor maximo de los grupos es ",e," y se encuentra en el Grupo_1")
else:
    if e == b:
        print("El valor maximo de los grupos es ",e," y se encuentra en el Grupo_2")
    else:
        if e == c:
            print("El valor maximo de los grupos es ",e," y se encuentra en el Grupo_3")
        else:
            print("El valor maximo de los grupos es ",e," y se encuentra en el Grupo_4")





