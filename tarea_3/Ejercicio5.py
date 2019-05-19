#Escriba un programa que permita crear una lista de palabras y que, a continuación,
# pida una palabra y elimine esa palabra de la lista.

Palabras = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra1 = str(input("Dígame la palabra 1: "))
Palabra2 = str(input("Dígame la palabra 2: "))
Palabra3 = str(input("Dígame la palabra 3: "))
Palabra4 = str(input("Dígame la palabra 4: "))

Lista_Palabras= [Palabra1,Palabra2,Palabra3,Palabra4]
print("La lista solicitada tiene: ",Palabras,"elementos y los siguientes elementos:",Lista_Palabras)

eliminar1 = str(input("Dígame la primera palabra que desea elminar: "))
eliminar2 = str(input("Dígame la segunda palabra que desea elminar: "))
eliminar3 = str(input("Dígame la tercer palabra que desea elminar: "))

while eliminar1 in Lista_Palabras:
  Lista_Palabras.remove(eliminar1)
  
while eliminar2 in Lista_Palabras:
  Lista_Palabras.remove(eliminar2)
while eliminar3 in Lista_Palabras:
  Lista_Palabras.remove(eliminar3)

print("La lista solicitada tiene: ",Palabras,"elementos y los siguientes elementos:",Lista_Palabras)