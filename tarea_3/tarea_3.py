# Para definir la agenda del hospital
agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
# agregamos una persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')]
# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)

[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor'), ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')]

# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]
# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor'), ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta'), ('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta'), ('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor'), ('Felipe', 'Perez', 12243151, 42, 65151111, 'documento'), ('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor'), ('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')]
# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)
('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')
('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')
('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta')
('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor')
('Felipe', 'Perez', 12243151, 42, 65151111, 'documento')
('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor')
('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')

#1 Cuantos pacientes llegaron en total?
print("En total llegaron ", len(persona)," personas")

Persona1= persona [0]
Persona2= persona [1]
Persona3= persona [2]
Persona4= persona [3]
Persona5= persona [4]

#2 Cuantas personas llegan con dolor?

Enfermedad = [ Persona1 [5],Persona2 [5],Persona3 [5],Persona4 [5],Persona5 [5] ].count('dolor')

print("En total ",Enfermedad," personas llegaron con dolor")

#3 Ordenar de menor a mayor?

numbers = [ Persona1 [3],Persona2 [3],Persona3 [3],Persona4 [3],Persona5 [3] ]
sorted_numbers =  sorted (numbers)
print ( 'Edades originales: {} , Edades ordenadas de mayor a menor: {} ' .format (numbers, sorted_numbers))

#4 Cuantas pesonas son mayores de edad?

numbers = list(filter(lambda x: x > 18, numbers))
print("Las siguientes edades son mayores de 18 años: ",numbers, "y en total son: ",len(numbers))

numbers = [ Persona1 [3],Persona2 [3],Persona3 [3],Persona4 [3],Persona5 [3] ]
numbers = list(filter(lambda x: x < 18, numbers))
print("Las siguientes edades son menores de 18 años: ",numbers, "y en total son: ",len(numbers))

#5 Ordenar  empezando por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el adulto mayor

Lista_prioridades = [ Persona1 [5],Persona2 [5],Persona3 [5],Persona4 [5],Persona5 [5] ]

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

