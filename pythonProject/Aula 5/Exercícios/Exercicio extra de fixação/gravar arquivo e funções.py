def testeArquivo(nomeArquivo):
    """
    Função que testa se o arquivo txt existe e retorna Falso ou Verdadeiro
    :param nomeArquivo: nome do arquivo TXT que foi criado conforme programa principal
    :return: False para arquivo inexistente e True para arquivo valido
    """
    try:
        a = open(nomeArquivo,'rt')
    except FileNotFoundError:
        print('Arquivo de lista não existe...\n')
        return False
    else:
        a.close()
        return True

def criarArquivo(nomeArquivo):
    """
    Função que cria o arquivo txt com nome da variavel nomeArquivo
    :param nomeArquivo: variavel de nome conforme programa principal
    :return: nome do arquivo
    """
    try:
        a = open(nomeArquivo,'wt+')
    except:
        testeArquivo(nomeArquivo)
    else:
        print('Arquivo {} Criado'.format(nomeArquivo))
    finally:
        a.close()

def adicionarNome(nomeArquivo,nome,idade):
    """
    Função para escrever 2 variavel, nome e idade, em nomeArquivo informado no codigo principal
    testa idade se for número inteiro, caso contrario repete a função.
    :param nomeArquivo:
    :return:
    """
    try:
        a = open(nomeArquivo,'at')
    except:
        print('Erro ao abrir arquivo para adicionar nome')
    else:
        if idade == 1:
            print(a.write('{} : {} ano\n'.format(nome, idade)))
        else:
            print(a.write('{} : {} anos\n'.format(nome , idade)))
    finally:
        a.close()

def lista(nomeArquivo):
    """
    Função para leitura e print de nomeArquivo informado no programa principal.
    :param nomeArquivo:
    :return: retorna print do arquivo texto total.
    """
    try:
        a = open(nomeArquivo,'rt')
    except:
        print('Erro ao abrir lista')
    else:
        print(a.read())
    finally:
        a.close()


#Programa principal
arquivo = 'namelist.txt'
if not testeArquivo(arquivo):
    criarArquivo(arquivo)
else:
    print('Arquivo {} Localizado. Iniciando...\n'.format(arquivo))
print('Codigo criado por Marco Antônio de Souza Matos, Armazenamento de lista')
while True:
    print('+', '-' *26, '+')
    print('|', '-' *10, 'MENU', '-'*10, '|')
    print('+', '-' *26, '+')
    print('* Adicionar \n'
          '* Listar nomes\n'
          '* Sair')
    res = input('Escreva a opção desejada: ')
    res = res.upper()

    if res == 'ADICIONAR':
        print('- Foi selecionado opção de adição de nomes: \n')
        while True:
            nome = input('Escreva o nome: ')
            try:
                idade = int(input('Escreva a idade: '))
            except:
                print('A idade precisa ser um número inteiro')
            else:
                if idade > 0 and idade < 120:
                    adicionarNome(arquivo,nome,idade)
                    repeticao = input('deseja adicionar um novo? escreva sim para adicionar ou escreva qualquer outra coisa para voltar: ')
                    repeticao = repeticao.upper()
                else:
                    print('a idade precisa ser maior que 0 e menor que 120')
                    continue

            if repeticao == 'SIM':
                continue
            else:
                break




    elif res == 'LISTA' or  res == 'LISTAS' or res == 'LISTAR' or  res == 'LISTAR NOMES':
        print('- Foi selecionado opção de listar nomes: \n ')
        lista(arquivo)
        while True:
            rep = input('Escreva "voltar" para ir ao menu principal, ou escreva sair para encerrar o programa: ')
            rep = rep.upper()
            if rep == 'SAIR':
                break
                res = 'SAIR'
            if rep == 'VOLTAR':
                res = 'MENU'
                break
        if res == 'SAIR' or rep == 'SAIR':
            print('Encerrando o programa...')
            break



    elif res == 'SAIR': # Para finalizar o programa
        print('Encerrando o programa...')
        break

    else: #em caso de qualquer comando não reconhecido :
        print('Comando invalido')
    if res == 'MENU':
         continue