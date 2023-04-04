#LISTA
#EXEMPLO: amigos = [Paulo, 2, False]

num_sor = [16, 8, 4, 2, 32]
amigos = ["Paulo", "Karen", "James", "Xico", "Xico", "Deco", "Deko"]
amigos2 = amigos.copy()

amigos.sort()
num_sor.sort()
#num_sor.reverse()
amigos.extend(num_sor)
amigos.append("Carlos, Maria")
#amigos.insert(1, "Carlinha") -> ADICIONA MAIS UM NA LISTA
amigos.remove("Deko")
#amigos.clear() -> LIMPA A LISTA
#amigos.pop() -> MOSTRA ITENS ALEATORIOS DA LISTA
#amigos[1] = "Carmen" -> SUBSTITUI A VARIÁVEL
print(amigos.index("James"))
print(num_sor.index(4))
print(amigos.count("Xico"))

print(amigos[0])
print(amigos[2])
print(amigos[4])
print(amigos[0:])
print(amigos[0:3])
print(amigos[3:5])

print(amigos2)

