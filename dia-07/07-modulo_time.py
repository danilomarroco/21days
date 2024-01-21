import time

print('Bem vindo ao temporizador')
opcao = input('Escolha uma opção:\n 1 - Temporizador \n 2 - Regressivo\n')
tempo = int(input('Digite o tempo desejado: '))

# if opcao == '1':
#     print('Opção escolhida Temporizador!\n')
#     for i in range(tempo):
#         time.sleep(1)
#         print(i + 1)
# if opcao == '2':
#     print('Opção Escolhida Regressivo')
#     for i in range(tempo):
#         time.sleep(1)
#         print(tempo)
#         tempo -= 1

if opcao == '1':
    print('Opção escolhida Temporizador!\n')
    for i in range(1, tempo + 1):
        time.sleep(1)
        print(i)
if opcao == '2':
    print('Opção Escolhida Regressivo')
    for i in range(tempo, 0, -1):
        time.sleep(1)
        print(i)
