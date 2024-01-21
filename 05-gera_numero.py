import random

# aleatorio = random.randint(1, 60)

lista = []

# for i in range(6):
#     aleatorio = random.randint(1, 60)
#     if aleatorio in lista:
#         aleatorio = random.randint(1, 60)
#         lista.append(aleatorio)
#     else:
#         lista.append(aleatorio)

# lista.sort()
# print(lista)





while len(lista) < 6 :
    aleatorio = random.randint(1, 60)
    if aleatorio  in lista:
        aleatorio = random.randint(1, 60)
        lista.append(aleatorio)
    else:
        lista.append(aleatorio)

lista.sort()
print("#" * 40)
print("##    Gerador de jogo da mega sena    ##")
print("#" * 40)
print("##                                    ##")
print("##                                    ##")
print(f'##      {lista}       ##')
print("##                                    ##")
print("##                                    ##")
print("#" * 40)