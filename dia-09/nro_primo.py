import random

pontuacao = 0

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ver_pontuacao(pontuacao):
    print(f'Sua pontuação é: {pontuacao}')

def zerar_pontuacao(pontuacao):
    pontuacao = 0
    return pontuacao




while True:
    numero = random.randint(1, 100)
    print('\nBem vindo ao jogo dos numeros primos!\n\n')
    print('#' * 92)
    print('###      Instruções                                                                      ###')
    print('###      Vou gerar um numero aleatório e você vai identificar se ele é primo ou não      ###')
    print('###      Respondendo Primo e Não Primo                                                   ###')
    print('###      A cada resposta certa ganha um ponto e continua no jogo                         ###')
    print('###      Se responder errado o jogo é encerrado                                          ###')
    print('#' * 92)
    print('\n Escolha uma opção:\n 1 - JOGAR\n 2 - PONTUACAO\n 3 - ZERAR PONTOS\n 4 - SAIR\n')
    opcao = input('Opção: ')

    match opcao:
        case '1':
            print('\nVamos jogar!\n\n Vou gerar um numero aleátorio e você vai responder com as seguintes opções:\n\n Primo e Não Primo\n\n')
            print(f'O numero é: {numero}\n\n')
            print(eh_primo(numero))
            resposta = input("\nÉ primo (P) ou não primo (N)? ").strip().lower()
            if (eh_primo(numero) and resposta == 'p') or (resposta == 'n' and not eh_primo(numero)):
                pontuacao += 1
                print(f'\nParabens você acertou!!\n\n Marcou um ponto, sua pontuação é: {pontuacao}!!')
            else:
                print(f'\nVocê errou, jogo encerrado!!')
                break
        case '2':
            ver_pontuacao(pontuacao)
        case '3':
            pontuacao = 0
            print('Pontuação zerada!')
        case '4':
            break