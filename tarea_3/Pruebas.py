#3 Ordenar de menor a mayor?
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)


personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]
menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)


lista = [2, 3, 1, 5, 1, 7, 8, 8, 9, 15, 1, 1]
lista = list(filter(lambda x: x < 2, lista))
print(lista)

Palabras = int(input("Dígame cuántas palabras tiene la lista: "))
Palabra1 = str(input("Dígame la palabra 1: "))
Palabra2 = str(input("Dígame la palabra 2: "))
Palabra3 = str(input("Dígame la palabra 3: "))

Lista_Palabras= [Palabra1,Palabra2,Palabra3]
print("La lista solicitada tiene: ",Palabras," y los siguientes elementos:",Lista_Palabras)
