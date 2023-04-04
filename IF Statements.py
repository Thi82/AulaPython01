# IF STATEMENTS

is_male = True
is_tall = True

if is_male and is_tall: #AS DUAS CONDIÇÕES DEVEM SER IGUAIS (and)
    print("You are a tall male")
elif is_male and not(is_tall): #SE FOR MALE, MAS NÃO TALL
    print("You are male, but not tall")
elif not(is_male) and is_tall: #SE NÃO FOR MALE, MAS FOR TALL
    print("You are not male, but you are tall")
else:
    print("You are neither male or tall")

print("*************************************************")

#CRIANDO MAIS FUNÇÕES
def max_num(num1, num2, num3):
    #if num1 == num2 and num1 == num3: # EQUAL
    #f num1 != num2 and num1 != num3: # NOT EQUALS
    #if num1 <= num2 and num1 >= num3: # MENOR OU IGUAL QUE

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
  # elif num3 >= num1 and num3 >= num2:
    else:
        return num3

print(max_num(3, 4, 5))

print("*************************************************")

