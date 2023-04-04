#VARIAVEIS COM STRING
Nome1 = "Maria"
Nome2 = "Paulo"
Nome3 = "Julio"
Idade1 = "45"
Idade2 = "18"
Idade3 = "50"
Local1 = "Floresta"
Local2 = "Praia"

#BOOLEAN
isMale = False
isFemale = True

#VARIAVEL DIRETA:
var1 = "GODZILLA"
var2 = "jaspion"
print(var1)
print(var2)

#CONCATENATION
print(var2 + " é legal")

#FUNCTIONS
print(var1.lower())
print(var2.upper())

#PERGUNTANDO SE A FUNÇÃO É:
print(var1.islower())
print(var2.isupper())

print(var1.upper().islower())
print(var2.upper().isupper())

#INFORMA QUANTIDADE DE LETRAS
print(len(var1))
print(len(var2))

#IMPRIME O INDEX, SENDO QUE 0 ZERO É A PRIMEIRA LETRA:
print(var2[0].upper())
print(var2[1])
print(var2[2])
print(var2[3])
print(var2[4])
print(var2[5])
print(var2[6])

#VALOR DO INDEX IMPRESSO:
print(var1.index("Z"))
print(var1.index("GOD"))
print(var1.index("LLA"))

# SUBSTITUI CERTA PALAVRA/DADO:
print(var1.replace("GOD", "MONGO"))
print(var2.replace("jaspion", "Changeman"))

#VARIAVEL PODE SER MUDADA NO MEIO DO PROCESSO:
Idade3 = "20"

print("" + Nome1 + " andava na " + Local1 + "")
print("Tinha " + Idade3 + " anos nesta época")
print("Quando " + Nome3 + " reapareceu")

#PULA LINHA
print("Girafa\nMacaco\nMosquito")

# BACKSLASH ADICIONA INFORMAÇÃO APÓS:
print("Cachorro\. Gato")
print("Cachorro\1 Gato")
print("Cachorro Gato")
print("Cachorro\      Gato")

#NUMEROS
print(2.5765)
print(-6747)
print(2 + 5)
print(2.35 + 7.80 * 2)
print(5 - 14)
print(89234 + 2345 - 36789)
print(8 * 2 + 5)
print(8 * (2 + 5))
print((8 * 2) - (5 + 5))
print(300 / 2)
print(2 * 6876)

#MODULO // Primeiro Dividido pelo segundo, mostra o RESTANTE
print(10 % 3)
print(20 % 3)
print(180 % 2)
print(10.5 % 5)

#NUMEROS DENTRO DE VARIAVEIS
myAge = 20
myAge2 = -5
yourAge = 35
herAge = 50

print(myAge)
print(myAge, yourAge, herAge)
print(myAge / yourAge)
print(myAge * yourAge - herAge)

#CONVERTE EM STRING
print(str(myAge) + " é a minha idade")
print("" + str(myAge) + " é a minha idade, enquanto ela tem " + str(herAge) + "")

#FUNÇÕES E NÚMEROS

#abs VALOR ABSOLUTO
print(abs(myAge2))

#pow QUADRADO (POWER OF TWO)
print(pow(3, 2))
print(pow(6, 2))
print(pow(2, 3))

#max MOSTRA MAIOR NÚMERO
#min MOSTRA MENOR NÚMERO
print(max(2, 6, 4))
print(min(2, 6, 4))

#round ARREDONDA BASEADO NO MEIO (5)
print(round(3.1))
print(round(3.3))
print(round(3.4))
print(round(3.6))
print(round(3.8))
print(round(4.0))

#IMPORTA FUNÇÃO EXTRA (MODULO)
from math import *

#floor ARRENDONDA PRA BAIXO
print(floor(5.1))
print(floor(5.3))
print(floor(5.4))
print(floor(5.6))
print(floor(5.8))
print(floor(6.0))

#ceil ARRENDONDA PRA CIMA
print(ceil(5.1))
print(ceil(5.3))
print(ceil(5.4))
print(ceil(5.6))
print(ceil(5.8))
print(ceil(6.1))

#sqrt RAIZ QUADRADA
print(sqrt(36))
print(sqrt(24))
print(sqrt(120))

#INPUT DE UM USUÁRIO (pega o que o usuário colocar, e transforma na variável "nome_input")

nome_input = input("Por favor, nos diga seu nome: ")
idade_input = input("Qual a sua idade?: ")
print("Olá " + nome_input + " seja bem-vindo! " + "Sua idade é " + idade_input + "")