print("#" * 40)
print("##     Calculadora simples v1.0       ##")
print("#" * 40)

def calcular(operacao, n1, n2):
    if operacao == '/' and n2 == 0:
        return "Não é possivel realizar a divisão por zero!!"
    
    operacoes = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x / y
    }
    return operacoes.get(operacao, lambda x,y: "Operação Inválida")(n1,n2)
        
num1 = float(input("Digite o primeiro numero: "))
oper = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo numero: "))

print(f'Resultado: {calcular(oper, num1, num2)}')
