#Exercício 2:
'''
Suponha que você é um colecionador de jogos de videogame. Escreva um algoritmo que permita cadastrar esses
jogos informando o nome e a qual vídeogame ele pertence.

Para isso, crie um menu de opções contendo:
Cadastrar novo item
Listar tudo que foi cadastrado
Sair

Para resolver esse exercício, crie pelo menos uma função para cada item do menu

Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco
e manter os dados cadastrados.
'''


'''
def cadastro():


def listar():


def sair():

'''

#  Programa Principal
print('Bem vindo!')
print('Sistema de colecionador de jogos criado por Marco Antônio de Souza Matos')
while True:
    print('+', '-' * 20, '+')
    print('|', ' ' * 7, 'MENU', ' ' * 7, '|')
    print('+', '-' * 20, '+')
    print('* Cadastrar \n'
          '* Listar jogos \n'
          '* Sair')
    opcao = input('Selecione a opção desejada: ')
    menu = opcao.upper()

    if menu == 'LISTA' or menu == 'LISTAR' or menu == 'JOGOS' or menu == 'LISTA DE JOGOS' or menu == 'LISTAR JOGOS':
        print('Lista de jogos:')
        # incremento futuro
        print(' ')
        print('_ ')
        retorno = 0
        while retorno != 'SAIR':
            retorno = input('Escreva "voltar" para voltar ao menu principal, ou escreva "sair" para fechar o programa')
            retorno = retorno.upper()
            if retorno == 'VOLTAR':
                menu = 'VOLTAR'
                break

            if retorno == 'SAIR':
                menu = 'SAIR'
                break


    if menu == 'CADASTRO' or menu == 'CADASTRAR':
        print('Cadastro de novo jogo')
        jogo = 0
        while jogo != 'SAIR':
            jogo = input('Escreva "novo" para adicionar um jogo novo, ou "voltar" para voltar ao menu principal, ou escreva "sair" para fechar o programa')
            jogo = jogo.upper()
            if jogo == 'NOVO':
                #novo = cadastro()
                print('novo cadastro: ')
                continue
            if jogo == 'VOLTAR':
                menu = 'VOLTAR'
                break
            if jogo == 'SAIR':
                menu = 'SAIR'
                break



    if menu == 'SAIR':
        print("Encerrando o programa...")
        break
    if menu == 'VOLTAR':
        continue
    else:
        print('opção invalida...')
        continue

