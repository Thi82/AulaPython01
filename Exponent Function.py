#print(2**3)

def power_raise(base_num, pow_num):
    resultado = 1
    for index in range(pow_num):
        resultado = resultado * base_num
    return resultado

print(power_raise(2, 3))