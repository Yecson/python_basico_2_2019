# Información de los pacientes


#identificación
#Nombre
#Apellido
#teléfono
#dirección
#lista de enfermedades tratadas
#lista de medicamentos que toma

directorio = []

telefonos = {}
nombres = {}
apellidos = {}
direcciones = {}
enfermedades = {}
medicamentos = {}

print("Agregar Nombre, telefono, Enfermedad y Medicamento")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
telefono = input("Telefono: ")
direccion = input("Direccion: ")
enfermedad = input("Enfermedad: ")
medicamento = input("Medicamento: ")


telefonos[nombre] = telefono
nombres[telefono] = nombre
enfermedades[enfermedad] = nombre

directorio.append([nombre, telefono, enfermedad, medicamento])

print(directorio)
