# pida una palabra y elimine esa palabra de la lista.

Palabras = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra1 = str(input("Dígame la palabra 1: "))
Palabra2 = str(input("Dígame la palabra 2: "))
Palabra3 = str(input("Dígame la palabra 3: "))
Palabra4 = str(input("Dígame la palabra 4: "))

a = [Palabra1,Palabra2,Palabra3,Palabra4]


Palabras1 = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra5 = str(input("Dígame la palabra 1: "))
Palabra6 = str(input("Dígame la palabra 2: "))
Palabra7 = str(input("Dígame la palabra 3: "))

b = [Palabra5,Palabra6,Palabra7]

print("La lista final es ",list(set(a)))

print("Las palabras que están en las 2 liastas son ",a & b)
print("Las palabras que están en solo en a ",a - b)
print("Las palabras que están en solo en b ",b - a)
print("Las palabras que están en ambas listas son ",a | b)


