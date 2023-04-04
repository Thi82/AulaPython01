#open("lista_funcionarios.txt", "r") # read LER
#open("lista_funcionarios.txt", "w") # write ESCREVER
#open("lista_funcionarios.txt", "a") # append ACRESCENTAR
#open("lista_funcionarios.txt", "r+") # ler e escrever

#arq_funcionarios = open("lista_funcionarios.txt", "r") # read LER

#print(arq_funcionarios.readline(0)) #0 é nada, nada é tudo. Número mostra quantidade a ser mostrada
#print(arq_funcionarios.readline(2))

#Abaixo, imprime uma linha por vez
#print(arq_funcionarios.readline())
#print(arq_funcionarios.readline())

#print(arq_funcionarios.readline())

#print(arq_funcionarios.readable()) #Arquivo pode ser lido? True or False?
#print(arq_funcionarios.read()) #Lê o arquivo
#print(arq_funcionarios.readlines()) #Lê estilo LISTA

#for funcionario in arq_funcionarios.readlines():
    #print(arq_funcionarios.readlines()[1]) #Lê a posição INDEX
    #print(funcionario)
#arq_funcionarios.close()

#-------------------------------------------------#
#ABAIXO, REESCREVE "append" "a"
'''
arq_funcionarios = open("lista_funcionarios.txt", "a")
arq_funcionarios.write("ITEM NOVO") #Se tiver linha "livre" no arquivo somente.
arq_funcionarios.write("\nITEM NOVO") #Adiciona já criando uma linha nova.
arq_funcionarios.close()
'''

#Abaixo, reescreve o arquivo inteiro
arq_funcionarios = open("lista_funcionarios.txt", "w")
#arq_funcionarios.write("w Reescreve o arquivo inteiro") #Se tiver linha "livre" no arquivo somente.
arq_funcionarios.write(
    "w Reescreve o arquivo inteiro"
    "\n1º Linha"
    "\n2 ºLinha"
    "\n3º Linha"
    "\n4º Linha"
    "\n5º Linha"
)
arq_funcionarios.close()

# ABAIXO, cria um segundo arquivo de funcionários.
# SE o arquivo especificado no open possuir nome diferente

arq_funcionarios = open("lista_funcionarios2.txt", "w")
arq_funcionarios.write(
    "Kelly - Vendedora Junior"
    "\nPaulo - Porteiro"
    "\nJosé - Sorveteiro"
    "\nWagner - Vendedor de picolé"
    "\nSamara - Fantasma"
)
arq_funcionarios.close()

#ABAIXO, um arquivo html, com código configurado

arq_funcionarios = open("pagina_home.hmtl", "w")
arq_funcionarios.write("<p>Isto é HTML<\p>")
arq_funcionarios.close()
