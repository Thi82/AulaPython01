# ABAIXO, traz herança de Chef.py

from Chef import Chef

#class ChefFrances:
class ChefFrances(Chef):
    def galinha(self):
        print("Por favor, peça para o chef servir galinha.")

    def salada(self):
        print("Por favor, peça para o chef preparar uma salada.")

    def peixe(self):
        print("Por favor, pergunte ao chef se o peixe está pronto.")

    def ratatouille(self):
        print("Por favor, peça ao chef francês para fazer um ratatouille.")

    def vinho(self):
        print("Por favor, nos traga seu melhor vinho francês.")

    def galinha(self): #Só pode ser usado porque está herando isso de Chef.py
        print("Diga ao chef francês para fazer galinha, como o chef antigo fazia.")