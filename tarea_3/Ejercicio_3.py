#Escriba un programa que permita crear una lista de palabras y que, a
# continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

Palabras = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra1 = str(input("Dígame la palabra 1: "))
Palabra2 = str(input("Dígame la palabra 2: "))
Palabra3 = str(input("Dígame la palabra 3: "))
Palabra4 = str(input("Dígame la palabra 4: "))

Lista_Palabras= [Palabra1,Palabra2,Palabra3,Palabra4]
print("La lista solicitada tiene: ",Palabras,"elementos y los siguientes elementos:",Lista_Palabras)

eliminar = str(input("Dígame la palabra desea elminar: "))

while eliminar in Lista_Palabras:
  Lista_Palabras.remove(eliminar)

agregar = str(input("Dígame la palabra desea reemplazar:"))

Lista_Palabras.append(agregar)

print("La palabra: ",agregar,"sustituye a la palabra",eliminar,", la lista resultante es",Lista_Palabras)