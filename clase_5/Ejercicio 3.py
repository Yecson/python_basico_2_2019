# la palabra reservada para crear una nueva clase es class

class First:
    def __init__(self): #se usa para inicializar las clases
        print("contructor ")
f=First()

#--------------------------------------------------------------
#Crear un pato
#--------------------------------------------------------------

class Duck:
    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("walk like a duck")

#-------------------------------------------------------------
#al final puede crearse una instancia de pato llamado donald
#Para que donald pueda decir quacl y caminar
#------------------------------------------------------------

#Nace un pato llamado Donald
donald= Duck()
#Donald dice quack y camina
donald.quack()
donald.walk()
