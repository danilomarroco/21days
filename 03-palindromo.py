

texto = input('Digite uma palavra ou frase: ').lower().replace(' ', '').replace(',',"").replace('!',"").replace('?',"")
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print(f'Parabens você digitou um palindromo {texto_invertido}')
else:
    print(f'Sua palavra não é um palindromo {texto_invertido}')

# print(texto.lower().replace(' ', ''))
# print(texto_invertido.lower())
