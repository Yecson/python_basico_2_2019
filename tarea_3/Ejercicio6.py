# pida una palabra y elimine esa palabra de la lista.

Palabras = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra1 = str(input("Dígame la palabra 1: "))
Palabra2 = str(input("Dígame la palabra 2: "))
Palabra3 = str(input("Dígame la palabra 3: "))
Palabra4 = str(input("Dígame la palabra 4: "))

Lista_Palabras= [Palabra1,Palabra2,Palabra3,Palabra4]
print("La lista solicitada tiene: ",Palabras,"elementos y los siguientes elementos:",Lista_Palabras)

Lista_Ordenada = [Lista_Palabras[3],Lista_Palabras[2],Lista_Palabras[1],Lista_Palabras[0]]

print("La lista solicitada tiene los siguientes elementos:",Lista_Ordenada)

