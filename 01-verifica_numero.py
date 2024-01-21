print("Bem vindo ao programa que verifica se o número é par ou impar!")

numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print("O numero digitado é PAR")
else:
    print("O numero digitado é IMPAR")

# Solução otimizada
# print("O número é par." if int(input("Digite um número: ")) % 2 == 0 else "O número é ímpar.")
