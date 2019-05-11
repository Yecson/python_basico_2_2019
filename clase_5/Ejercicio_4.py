# 1 crear clase bebe
# 2 declarar 4 acciones

# Crea la clase con las funciones que tiene dentro y luego las imboca
class Bebe:
    def __init__(self,nombre,edad): #se usa para inicializar las clases
        self.nombre_bebe = nombre
        self.edad= edad

    def respirar(self):
        print("respirar")

    def comer(self):
        print("comer")

    def llorar(self):
        print("llorar")

    def dormir(self):
        print("dormir")

    def crecer(self, edad=1):
        if (self, edad + edad) > 100:
                self.vivo = False

        else:
            self.edad += edad
            self.vivo = True


print("hola soy un {}"
        "tengo {} años".format(BEBE_1.nombre_bebe,
                                 BEBE_1.edad))  # format me permite sustuit las {} por los parametros que están en el format

