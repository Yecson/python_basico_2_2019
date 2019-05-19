# Segunda parte

Palabras = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra1 = str(input("Dígame la palabra 1: "))
Palabra2 = str(input("Dígame la palabra 2: "))
Palabra3 = str(input("Dígame la palabra 3: "))

Lista_Palabras= [Palabra1,Palabra2,Palabra3]
print("La lista solicitada tiene: ",Palabras,"elementos y los siguientes elementos:",Lista_Palabras)

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
print(f"Ha escrito el número {numero}")