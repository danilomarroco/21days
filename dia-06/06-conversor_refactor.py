km_to_mil = 0.621371
mil_to_km = 1.60934
mt_to_pes = 3.28084
pes_to_mt = 0.3048

def converter_unidades(opcao, valor):
    conversoes = {
        '1' : lambda v: v * 0.621371,
        '2' : lambda v: v * 1.60934,
        '3' : lambda v: v * 3.28084,
        '4' : lambda v: v * 0.3048,
        '5' : lambda v: v * 9/5 + 32,
        '6' : lambda v: (v - 32) * 5/9

    } 
    return conversoes.get(opcao, lambda v: "Opção Inválida")(valor)

print('Conversor de unidades\n')


operacao = (input("Escolha a conversão: \n1. Quilômetros para Milhas \n2. Milhas para Quilômetros \n3. Metros para Pés \n4. Pés para Metros \n5. Celsius para Fahrenheit \n6. Fahrenheit para Celsius \nDigite o número da opção: "))

valor = int(input('Digite o valor a ser convertido: '))

print(f'Resultado da conversão: {converter_unidades(operacao, valor)}')

# match operacao:
#     case 1:
#         print(f'\nConvertendo {valor} km(s) para milha(s)\n')
#         convertido = float(valor * km_to_mil)
#         print(f'Resultado: {valor} km(s) são {convertido} milha(s)')
#     case 2:
#         print(f'\nConvertendo {valor} milhas(s) para km(s)\n')
#         convertido = float(valor * mil_to_km)
#         print(f'Resultado: {valor} milhas(s) são {convertido} km(s)')
#     case 3:
#         print(f'\nConvertendo {valor} metro(s) para pé(s)\n')
#         convertido = float(valor * mt_to_pes)
#         print(f'Resultado: {valor} metros(s) são {convertido} pés(s)')
#     case 4:
#         print(f'\nConvertendo {valor} pé(s) para metro(s)\n')
#         convertido = float(valor * pes_to_mt)
#         print(f'Resultado: {valor} pé(s) são {convertido} metro(s)')
#     case 5:
#         print(f'\nConvertendo {valor} Celsius para Fahrenheit\n')
#         convertido = float((valor * 9/5) + 32)
#         print(f'Resultado: {valor} Celsius são {convertido} Fahrenheit')
#     case 6:
#         print(f'\nConvertendo {valor} Fahrenheit para Celsius\n')
#         convertido = float((valor - 32) * 5/9)
#         print(f'Resultado: {valor} Fahrenheit são {convertido} Celsius')
