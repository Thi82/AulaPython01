# TRADUTOR DE LINGUAGEM BADALHOCA, ONDE VOGAIS VIRAM A LETRA "B"

def translate(frase):
    tradutor = ""
    for letra in frase:
#       if letra in "AEIOU":
#            tradutor = tradutor + "B"
#       if letra in "aeiou":
#            tradutor = tradutor + "b"
        if letra.lower() in "aeiou":
            if letra.isupper():
                tradutor = tradutor + "B"
            else:
                tradutor = tradutor + "b"
        else:
            tradutor = tradutor + letra
    return tradutor

print(translate(input("Insira uma palavra ou frase: ")))