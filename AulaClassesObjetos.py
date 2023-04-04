#CLASSES E OBJETOS
# ABAIXO, uma classe chamada Estudante:
# OBJETO será invocado na aba AulaClassesObjetos2.py

class Estudante:

    def __init__(self, nome, diretor, notamedia, recupera):
        self.nome = nome
        self.diretor = diretor
        self.notamedia = notamedia
        self.recupera = recupera

    def hall_da_fama(self):
        if self.notamedia >= 5.0:
            return True
        else:
            return False