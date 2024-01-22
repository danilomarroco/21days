tarefas = []

def cadastra_tarefa(novo_item):
    tarefas.append(novo_item)
    return print('TAREFA CADASTRADA COM SUCESSO!!\n')

def listar_tarefas():
    if len(tarefas) == 0:
        print('NÃO EXISTEM TAREFAS NA LISTA\n')
    else:
        print(list(enumerate(tarefas, start=1)))

def remove_tarefa(nro_tarefa):
    if nro_tarefa < len(tarefas) and nro_tarefa >= 0:
        tarefas.pop(nro_tarefa)
        return print('TAREFA EXCLUIDA COM SUCESSO!!\n')
    else:
        print('TAREFA NÃO ENCONTRADA!\n')    

# cadastra_tarefa('Comprar sabonete')
# cadastra_tarefa('Comprar macarrão')
# cadastra_tarefa('Fazer a barba')
# listar_tarefas()
# print(len(tarefas))
# remove_tarefa(2)
# print(len(tarefas))
# listar_tarefas()


print('###   Bem vindo ao gerenciador de tarefas simples v1.0   ###\n')
while True:
    print('#' * 32)
    print('###   Selecione uma opção:   ###\n###   1 - CADASTRAR TAREFA   ###\n###   2 - EXCLUIR TAREFA     ###\n###   3 - LISTAR TAREFAS     ###\n###   4 - SAIR               ###')
    print('#' * 32)
    opcao = input('\nEscolha uma opção: ')
    
    match opcao:
        case '1':
            print('CADASTRO DE TAREFA!!\n')
            cadastra_tarefa(input('Informe o nome da tarefa: \n'))
        case '2':
            print('EXCLUSAO DE TAREFA!!\n')
            remove_tarefa(int(input('Informe o numero da tarefa a ser excluída: ')))
        case '3':
            print('LISTAR TAREFAS!!\n')
            listar_tarefas()
        case '4':
            print('Obrigado e volte sempre!!')
            break
        case _:
            print('\nOpção inválida\n')
