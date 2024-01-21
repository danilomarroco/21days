
def isPalindromo(texto):
    texto = texto.lower().replace(' ', '').replace(',',"").replace('!',"").replace('?',"")
    return texto == texto[::-1]

texto_usuario = input("Digite uma palavra ou frase: ")

print('É palindromo' if isPalindromo(texto_usuario) else 'Não é palindromo!')