
#Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

Palabras = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra1 = str(input("Dígame la palabra 1: "))
Palabra2 = str(input("Dígame la palabra 2: "))
Palabra3 = str(input("Dígame la palabra 3: "))
Palabra4 = str(input("Dígame la palabra 4: "))

Lista_Palabras= [Palabra1,Palabra2,Palabra3,Palabra4]
print("La lista solicitada tiene: ",Palabras,"elementos y los siguientes elementos:",Lista_Palabras)

Verificar = str(input("Dígame la palabra a buscar: "))

a= [Palabra1,Palabra2,Palabra3,Palabra4].count(Verificar)

if a < 1:
    print("La palabra: ",Verificar," no aparece en la lista")
else:
    print("La palabra: ",Verificar," aparece",a,"veces en la lista")


