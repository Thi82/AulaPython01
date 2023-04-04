# FUNCTIONS -> COLEÇÃO DE TAREFAS

def diga_oi():
    print("Olá usuário")

def formula():
    print(2.35 + 7.80 * 2)

def diga_nome(nome, idade):
    #print("Olá " + nome + ", sua idade atualmente é " + idade)
    print("Olá " + nome + ", sua idade atualmente é " + str(idade))

def cubo(num):
    return num * num * num

resultado = cubo(4)

def soma(num2):
    return num2 + num2

print("************")

diga_oi()
formula()
#diga_nome("César", "35")
#diga_nome("Marcos", "26")
diga_nome("César", 35)
diga_nome("Marcos", 26)

print("************")

print(cubo(3))
print(soma(25))
print(resultado)


