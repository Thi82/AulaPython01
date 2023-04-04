#CALCULADORA 1
#num1 = input("Insira um número: ")
#num2 = input("Insira outro número: ")
#result = float(num1) + float(num2)
#print(result)

#result = float(num1) + float(num2)
#print(result)

#CALCULADORA 2
num1 = float(input("Insira o primeiro número: "))
op = input("Insira a operação: ")
num2 = float(input("Insira o segundo número: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Operador inválido")
