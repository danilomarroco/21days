tarefas = []

def cadastra_tarefa(novo_item):
    tarefas.append(novo_item)
    return print('TAREFA CADASTRADA COM SUCESSO!!\n')

def listar_tarefas():
    if len(tarefas) > 0:
        print('Lista de Tarefas:')
        for indice, tarefa in enumerate(tarefas):
            print(f'{indice}. {tarefa}')
    else:
        print(list(enumerate(tarefas, start=1)))
        print('NÃO EXISTEM TAREFAS NA LISTA\n')

def remove_tarefa(tarefas):
    listar_tarefas()
    nro_tarefa = int(input("\nDigite o número da tarefa a ser removida: "))
    if 0 <= nro_tarefa < len(tarefas):
        tarefas.pop(nro_tarefa)
        return print('TAREFA EXCLUIDA COM SUCESSO!!\n')
    else:
        print('TAREFA NÃO ENCONTRADA!\n')    


print('###   Bem vindo ao gerenciador de tarefas simples v1.0   ###\n')
while True:
    print('#' * 32)
    print('###   Selecione uma opção:   ###\n###   1 - CADASTRAR TAREFA   ###\n###   2 - EXCLUIR TAREFA     ###\n###   3 - LISTAR TAREFAS     ###\n###   4 - SAIR               ###')
    print('#' * 32)
    opcao = input('\nEscolha uma opção: ')
    
    match opcao:
        case '1':
            print('\nCADASTRO DE TAREFA!!\n')
            cadastra_tarefa(input('Informe o nome da tarefa: \n'))
        case '2':
            print('\nEXCLUSAO DE TAREFA!!\n')
            remove_tarefa(tarefas)
        case '3':
            print('\nLISTAR TAREFAS!!\n')
            listar_tarefas()
        case '4':
            print('\nObrigado e volte sempre!!')
            break
        case _:
            print('\nOpção inválida\n')
