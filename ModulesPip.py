# MODULES permite que você importe
# Partes de um arquivo para outro
# Aqui, temos o que será usado em Modules2.py:

import random

feet_in_mile = 5280
metros_em_km = 1000
chocolates = ["Amargo", "Doce", "Cacau 50%","Branco"]

def arq_externo(nome_arquivo):
    return nome_arquivo[nome_arquivo.index(".") + 1:]

def rola_dado(numero):
    return random.randint(1, numero)