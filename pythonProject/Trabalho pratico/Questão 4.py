#Funções:

def cadastrar_funcionarios(funcionarios):
    nome = input('Insira o nome do funcionário: ')
    setor = input('Insira o setor do funcionário: ')
    if not funcionarios['id']:
        id = 1
    else:
        id = funcionarios['id'][-1] +1
    while True:
        try:
            salario = float(input('Insira o salário do funcionário: '))
        except:
            print('Ops! Ocorreu um erro, insira um valor numérico e sem o uso da virgula')
            continue
        else:
            break
    funcionarios['nome'].append(nome)
    funcionarios['setor'].append(setor.upper())
    funcionarios['salario'].append(salario)
    funcionarios['id'].append(id)
    print('*'*95) # espaçamento estérico


def consultar_funcionarios(funcionarios):
    while True:
        print('1. Consultar Todos os Funcionários\n'
              '2. Consultar Funcionário por ID\n'
              '3. Consultar funcionário(s) por Setor\n'
              '4. Retornar')
        try:
            menu = int(input('Digite a opção desejada: '))
        except:
            print('Ops!, utilize apenas números')
            continue
        else:
            if menu > 0 and menu <= 4 :
                return int(menu)
                break
            else:
                print('Número invalido, tente novamente..\n'
                      ' ')
                continue
        finally:
            print('*'*95) # espaçamento estérico


def remover_funcionario(funcionarios):
    """
    Função que valida se id é um número inteiro e fica em loot até inserir um numero inteiro
    :param funcionarios:
    :return: id
    """
    while True:
        try:
            id = int(input('Insira o ID do usuário para remover: '))
        except:
            print('Ops! Não entendi, insira o número de ID:')
            continue
        else:
            break
    print('*' * 95) # espaçamento estérico
    return id

#Programa inicial

#variaveis
funcionarios = {'id':[],'nome':[],'setor':[],'salario':[]}

#Menu informativo
print('+','-'*91,'+')
print('|           NewinfoRH - Software de gestão de pessoas: Marco Antônio de Souza Matos           |')# RU: 4316762
print('+','-'*91,'+')
print('')

#loop interativo
while True:
    print('Menu principal:\n'
          '1.	Cadastrar Funcionário\n'
          '2.	Consultar Funcionários(s)\n'
          '3.	Remover Funcionário\n'
          '4.	Sair')
    try:
        menu = int(input('Digite a opção desejada: '))
    except:
        print('Não consegui entender, utilize apenas números')
        continue
    else:   # se o teste de valor inteiro for verdadeiro,segue com o codigo:
        if menu == 4:#Opção de sair.
            break
        # Função de Cadastro
        elif menu == 1:
            print('*'*95) # espaçamento estérico
            print('Você selecionou a opção CADASTRAR FUNCIONÁRIOS:')
            cadastrar_funcionarios(funcionarios)
            continue
        # Função de consulta
        elif menu == 2:
            consultarmenu = consultar_funcionarios(funcionarios)
            # função de consultar todos os funcionários
            if consultarmenu == 1:
                print('*' * 95)  # espaçamento estérico
                print('Você escolheu: "Consultar todos os funcionários"\n'
                      ' ')
                for cont in funcionarios['id']:
                    tamanhoNome = int(len(funcionarios['nome'][cont -1]))
                    print('ID:{}   |  Nome: {}{} | Setor: {}  | Salario: R${}  |'.format
                                                                                (funcionarios['id'][cont - 1],
                                                                                 funcionarios['nome'][cont - 1],
                                                                                 ' '* (40 - tamanhoNome),
                                                                                 funcionarios['setor'][cont-1],
                                                                                 funcionarios['salario'][cont-1]))
                print('*'*95) # espaçamento estérico
                continue

            # função de consultar funcionário por ID
            elif consultarmenu == 2:
                print('*' * 95)  # espaçamento estérico
                print('você escolheu: "Consultar funcionário por ID')
                consulta_id = int(input('Insira o ID do funcionário: '))
                if consulta_id in funcionarios['id']:
                    print('Você selecionou o funcionário:\n'
                          
                          'ID:{}   |  Nome: {}  | Setor: {}  | Salario: R${}  |'.format(funcionarios['id'][consulta_id-1],
                                                                                        funcionarios['nome'][consulta_id-1],
                                                                                        funcionarios['setor'][consulta_id-1],
                                                                                        funcionarios['salario'][consulta_id-1]))

                else:
                    print('Usuário não encontrado!')
                    print('*' * 95) # espaçamento estérico
                    continue

            # CONSULTAR FUNCIONARIO POR SETOR
            elif consultarmenu == 3:
                print('você escolheu: "Consultar funcionário por Setor')
                consulta_setor = (input('Insira o setor desejado: '))
                print('*' * 95)  # espaçamento estérico
                if consulta_setor.upper() in funcionarios['setor']:
                    s = 0
                    print('Você selecionou o funcionário:')
                    for s in range (len(funcionarios['setor'])):
                        if funcionarios['setor'][s-1] == consulta_setor.upper():
                            print('ID:{}   |  Nome: {}  | Setor: {}  | Salario: R${}  |'.format(funcionarios['id'][s - 1],
                                                                                                funcionarios['nome'][s - 1],
                                                                                                funcionarios['setor'][s - 1],
                                                                                                funcionarios['salario'][s - 1]))

                else:
                    print('Usuário não encontrado!')
                    print('*' * 95) # espaçamento estérico
                    continue

            else:
                continue
        # REMOVER FUNCIONARIO
        elif menu == 3:
            print('*' * 95) # espaçamento estérico
            remove = remover_funcionario(funcionarios)
            if remove in funcionarios['id']:
                indice = funcionarios['id'].index(remove)
                print('indice:',indice)
                nome = funcionarios['nome'][remove-1]
                setor = funcionarios['setor'][remove-1]
                salario =funcionarios['salario'][remove-1]
                funcionarios['nome'].remove(indice)
                funcionarios['setor'].remove(indice)
                funcionarios['salario'].remove(indice)
                funcionarios['id'].remove(indice)
                print('Usuário removido com sucesso')
            else:
                print('Usuário não encontrado...')
                continue

        else:
            print('*' * 95) # espaçamento estérico
            print('Opção invalida')
            print(' ')
    print('*' * 95)  # espaçamento estérico