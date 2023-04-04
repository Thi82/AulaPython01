#REAÇÃO A ALGO COLOCADO NO LOCAL AO INVES DO NUMERO

try:
    valor = 10 / 0
    numero = int(input("Insira um número: "))
    print(numero)
except ZeroDivisionError as erro: #CRIA uma variável com o erro
    print("Erro: Divisão por zero")
except ValueError:
    print("Número Inválido")