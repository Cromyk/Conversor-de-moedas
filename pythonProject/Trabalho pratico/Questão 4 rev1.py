#variaveis
funcionario = []
codigo_funcionario = 0

#Funções:
def cadastrar_funcionario(codigo_funcionario):
    """
    Função invocada para criar um dicionário com as informações de id, nome, setor e salario de um funcionario
    em uma lista chamada 'funcionario' ( funcionario =[] )
    :param codigo_funcionario: nome:
                               setor:
                               salario:
                               lista = {}   // Dicionário que copia os dados do funcionário em uma lista.
    :return:
    """
    nome = input('Insira o nome do funcionário: ')
    setor = input('Insira o setor do funcionário: ')
    salario = float(input('Insira o salário do funcionário: '))
    lista = {'id': codigo_funcionario, 'nome': nome, 'setor': setor, 'salario': salario}  # crio um dicionário para uso
    funcionario.append(lista.copy()) #Faz uma cópia de dicionário dentro da lista funcionario,
                                     #ocupando o proximo indice disponivel
    print('*' * 80)  # espassamento estético
def consultar_funcionarios():
    """
    Função invocada para consultar a lista de funcionários: Dentro da função o codigo apresentará um menu com 4 opções
    de escolha: podendo escolher entre:   '1. Consultar Todos os Funcionários'
                                          '2. Consultar Funcionário por ID'
                                          '3. Consultar funcionário(s) por Setor'
                                          '4. Retornar

                1. Consultar Todos os Funcionários
                        Este parametro faz uma busca minerando a lista de funcionários e imprimindo cada indice (dicionário)
                        em uma variavel temporaria que por sua vez tambem é feito uma busca em todos os itens dentro do
                        dicionário e imprime todas as key e suas correspondentes value  no formato:  KEY : VALUE
                2. Consultar Funcionário por ID
                        Este parametro faz uma busca minerando a lista de funcionários e imprimindo cada indice (dicionário)
                        em uma variavel temporaria que por sua vez tambem é feito uma busca em todos os itens dentro do
                        dicionário e imprime somente o dicionário que contiver dentro da key 'id' o id correspondente
                        informado na coleta da resposta com o inport(), todas as key e suas correspondentes value
                         são impressas no formato:  KEY : VALUE
                3. Consultar funcionário(s) por Setor
                         Este parametro faz uma busca minerando a lista de funcionários e imprimindo cada indice (dicionário)
                        em uma variavel temporaria que por sua vez tambem é feito uma busca em todos os itens dentro do
                        dicionário e imprime somente o dicionário que contiver dentro da key 'setor' o setor correspondente
                        informado na coleta da resposta com o inport(), todas as key e suas correspondentes value
                         são impressas no formato:  KEY : VALUE
                4. Retornar
                        finaliza a função

    :return:
    """
    while True:
        #Menu informativo
        print(' \n'
              '1. Consultar Todos os Funcionários\n'
              '2. Consultar Funcionário por ID\n'
              '3. Consultar funcionário(s) por Setor\n'
              '4. Retornar\n'
              ' ')
        menu = input('Digite a opção desejada: ')

        #Opção de multipla escolha utilizando if elif e else
        if menu == '1':
            print('*'*80) # espassamento estético
            print('Você selecionou a consulta de TODOS OS FUNCIONÁRIOS: ')
            for i in funcionario:# varrer o
                print('-'*25) # espassamento estético
                for key,value in i.items():
                    print('{} : {}'.format(key,value))
            print('-' * 25)  # espassamento estético
            return #finaliza função

        elif menu == '2':
            print('*' * 80) # espassamento estético
            print('Você selecionou a consulta de FUNCIONÁRIO POR ID: ')
            id = int(input('Informe o ID para consulta: ')) #Entrada de número inteiro representando o ID do funcionário
            for codigo in funcionario: #Varre todos os indices e exporta dicionário do indice para 'codigo' e executa
                                       # codigo abaixo uma vez por indice na lista funcionario
                if codigo['id'] == id: # Testa dentro do dicionário exportado em codigo a key 'id' se é igual á id informado
                    print('-' * 25) # espassamento estético
                    for key, value in codigo.items(): # Varre e verifica todos os items do dicionário e imprime
                                                      # em key e value respectivamente para apresentar os valores
                        print('{} : {}'.format(key, value))
            print('-' * 80) # espassamento estético
            return #finaliza função

        elif menu == '3':
            print('*' * 80)# espassamento estético
            print('Você selecionou a consulta de FUNCIONÁRIO(S) POR SETOR: ')
            setor = input('Informe o SETOR para consulta: ')#Entrada de string representando o SETOR do funcionário
            for setores in funcionario:#Varre todos os indices e exporta dicionário do indice para 'setores' e executa
                                       # codigo abaixo uma vez por indice na lista funcionario
                if setores['setor'] == setor: # Testa dentro do dicionário exportado em codigo a key 'setor' se é igual á id informado
                        print('-' * 25) # espassamento estético
                        for key, value in setores.items(): # Varre e verifica todos os items do dicionário e imprime
                                                           # em key e value respectivamente para apresentar os valores
                            print('{} : {}'.format(key, value))
            print('-' * 25) # espassamento estético
            return #finaliza função

        elif menu == '4':  # Opção de retorno
            print('Retornando ao menu principal\n'
                  ' ')
            return #finaliza função
        else:
            print('Opção invalida')
            continue #volta ao loop while True da função

def remover_funcionario():
    """
    Função que valida se id é um número inteiro e fica em loop até inserir um número inteiro.
    :param funcionarios:
    :return: id
    """
    id = int(input('Insira o ID do usuário para remover: ')) #recebe o valor de id fornecido pelo usuário
    for codigo in funcionario:   #Varre todos os indices e exporta dicionário do indice para 'codigo' e executa
                                 # codigo abaixo uma vez por indice na lista funcionario
        if codigo['id'] == id: # Valida dentro do dicionário exportado em 'codigo' se o input id informado é valido
            print('-' * 25) # espassamento estético
            print('Usuário {} Removido com sucesso...'.format(codigo['nome']))
            funcionario.remove(codigo) # função para remover o item equivalente ao dicionário exportado em 'codigo'
    print('-' * 25)  # espassamento estético

    return #finaliza função

#Programa inicial

    #Menu informativo
print('+','-'*91,'+')
print('|           NewinfoRH - Software de gestão de pessoas: Marco Antônio de Souza Matos           |')# RU: 4316762
print('+','-'*91,'+')
print('')

    # Código principal
while True:
    print('Menu principal:\n'
          '1.	Cadastrar Funcionário\n'
          '2.	Consultar Funcionários(s)\n'
          '3.	Remover Funcionário\n'
          '4.	Sair')

    menu = input('Digite a opção desejada: ')
    #Opção de cadastro de funcionário
    if menu == '1':
        print('*' * 80)  # espassamento estético
        codigo_funcionario = codigo_funcionario + 1 # codigo id do funcionário sempre incrementando com valor inteiro
        print('Foi selecionado: CADASTRAR FUNCIONÁRIO')
        cadastrar_funcionario(codigo_funcionario)  #invoca função cadastrar_funcionario( ) exportando o número de id
    #Opção para consulta de funcionário
    elif menu == '2':
        print('*' * 80)  # espassamento estético
        print('Foi selecionado: CONSULTAR FUNCIONÁRIO')
        consultar_funcionarios() #invoca função consultar_funcionários()
    #opção para remover um funcionário
    elif menu == '3':
        print('*' * 80)  # espassamento estético
        print('Foi selecionado: REMOVER FUNCIONÁRIO')
        remover_funcionario() #invoca função remover_funcionários()
    #opção para encerrar o programa
    elif menu == '4':
        break
    else:
        print('Opção invalida...')
        print(' ')
        continue
    print('')
print('finalizando o programa....')
#fim do codigo