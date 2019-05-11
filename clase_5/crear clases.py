# 1 crear clase bebe
# 2 declarar 4 acciones

# Crea la clase con las funciones que tiene dentro y luego las imboca
class Bebe:
    def __init__(self,nombre): #se usa para inicializar las clases
        self.nombre_bebe = nombre

    def respirar(self):
        print("respirar")

    def comer(self):
        print("comer")

    def llorar(self):
        print("llorar")

    def dormir(self):
        print("dormir")

#Nace el bebe BEBE_1

BEBE_1= Bebe("Bebe_1")

print("Cual es tu nombre?",BEBE_1.nombre_bebe)

BEBE_1.llorar()
BEBE_1.comer()
BEBE_1.dormir()
BEBE_1.respirar()