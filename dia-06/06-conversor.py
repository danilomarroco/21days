# Utilize as taxas de conversão fornecidas para realizar os cálculos corretamente: 
# Quilômetros para Milhas (1 quilômetro = 0,621371 milhas), 
# Milhas para Quilômetros (1 milha = 1,60934 quilômetros), 
# Metros para Pés (1 metro = 3,28084 pés), 
# Pés para Metros (1 pé = 0,3048 metros), 
# Graus Celsius para Fahrenheit (Fahrenheit = Celsius * 9/5 + 32)
# Graus Fahrenheit para Celsius (Celsius = (Fahrenheit - 32) * 5/9)


km_to_mil = 0.621371
mil_to_km = 1.60934
mt_to_pes = 3.28084
pes_to_mt = 0.3048

# two_km = km_to_mil * 4

# print(two_km)

print('Conversor de unidades\n')
# print('1 - Converter KM para Milhas')
# print('2 - Converter Milha para KM')
# print('3 - Converter Metro para Pés')
# print('4 - Converter Pés para Metro')
# print('5 - Converter Celsius para Fahrenheit')
# print('6 - Converter Fahrenheit para Celsius\n')

operacao = int(input("Escolha a conversão: \n1. Quilômetros para Milhas \n2. Milhas para Quilômetros \n3. Metros para Pés \n4. Pés para Metros \n5. Celsius para Fahrenheit \n6. Fahrenheit para Celsius \nDigite o número da opção: "))

valor = int(input('Digite o valor a ser convertido: '))

match operacao:
    case 1:
        print(f'\nConvertendo {valor} km(s) para milha(s)\n')
        convertido = float(valor * km_to_mil)
        print(f'Resultado: {valor} km(s) são {convertido} milha(s)')
    case 2:
        print(f'\nConvertendo {valor} milhas(s) para km(s)\n')
        convertido = float(valor * mil_to_km)
        print(f'Resultado: {valor} milhas(s) são {convertido} km(s)')
    case 3:
        print(f'\nConvertendo {valor} metro(s) para pé(s)\n')
        convertido = float(valor * mt_to_pes)
        print(f'Resultado: {valor} metros(s) são {convertido} pés(s)')
    case 4:
        print(f'\nConvertendo {valor} pé(s) para metro(s)\n')
        convertido = float(valor * pes_to_mt)
        print(f'Resultado: {valor} pé(s) são {convertido} metro(s)')
    case 5:
        print(f'\nConvertendo {valor} Celsius para Fahrenheit\n')
        convertido = float((valor * 9/5) + 32)
        print(f'Resultado: {valor} Celsius são {convertido} Fahrenheit')
    case 6:
        print(f'\nConvertendo {valor} Fahrenheit para Celsius\n')
        convertido = float((valor - 32) * 5/9)
        print(f'Resultado: {valor} Fahrenheit são {convertido} Celsius')



# (0 °C × 9/5) + 32
        # (1 °F − 32) × 5/9