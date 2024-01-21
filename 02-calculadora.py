print("#" * 40)
print("##     Calculadora simples v1.0       ##")
print("#" * 40)
print("##                                    ##")
print("## Escolha uma operação abaixo:       ##")
print("##     1 - SOMA                       ##")
print("##     2 - SUBTRAÇÃO                  ##")
print("##     3 - MULTIPLICAÇÃO              ##")
print("##     4 - DIVISÃO                    ##")
print("#" * 40)
operacao = int(input("Qual opção desejada: "))
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

def somar(n1, n2):
    resultado = n1 + n2
    print(f"Resultado da operação soma é: {resultado}")

def subtrair(n1, n2):
    resultado = n1 - n2
    print(f"Resultado da operação subtração é: {resultado}")

def multiplicar(n1, n2):
    resultado = n1 * n2
    print(f"Resultado da operação multiplicação é: {resultado}" )

def dividir(n1, n2):
    if n2 == 0:
        print("Não é possivel realizar divisão por zero")
    else:
        resultado = n1 / n2
        print(f"Resultado da operação divisão é: {resultado}" )

match operacao:
    case 1:
        print(f"Realizando a soma de {n1} e {n2}!")
        somar(n1, n2)
    case 2:
        print(f"Realizando a subtração de {n1} e {n2}!")
        subtrair(n1, n2)
    case 3:
        print(f"Realizando a multiplicação de {n1} e {n2}!")
        multiplicar(n1,n2)
    case 4:
        print(f"Realizando a divisão de {n1} e {n2}!")
        dividir(n1, n2)
