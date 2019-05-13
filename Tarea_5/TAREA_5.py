#TAREA 5

#Basado en el ejemplo anterior, crear un Nieto Humano, basado en las habilidades aprendidas por el
# abuelo humano y transmitidas al padre Humano.
#Abuelo -> padre -> Nieto
#El abuelo trabaja. El padre es contador y el nieto es analista de negocios
#El nieto tiene que ir a trabajar, sabe de contabilidad es un analista de negocios


# Misc classes
class misc:
    def __repr__(self):
        # return the clase name
        return self.__class__.__name__

    def __str__(self):
        # return the clase name
        return self.__class__.__name__

class Abuelo(misc):
    def __init__(self, parentesco):
        self.parentesco = parentesco


    def trabaja(self):
        print(f'El {self} va a trabajar')


class Padre(Abuelo):
    def __init__(self):
        super().__init__(parentesco='Padre')
        self.trabajo = True

    #def jugar(self):
       # print(f'El {self.parentesco} está jugando')

    def profesion(self):
        print(f'El {self.parentesco} sabe de contabilidad')

        class Nieto(Padre):
            def __init__(self):
                self.parentesco = 'Nieto'
                self.trabajo = True



class Nieto(Padre):
    def __init__(self):
        self.parentesco = 'Nieto'
        self.trabajo = True

    def hace(self):
        if not self.hace:
            print(f'El {self.parentesco} no es un analista de negocios')
        else:
            print(f'El {self.parentesco} es un analista de negocios')

Humano = Nieto()
print(Humano)

Humano.trabaja()

Humano.profesion()

Humano.hace()