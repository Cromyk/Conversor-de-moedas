def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
        except ValueError:
            print('opção invalida')
            continue
        else:
            break
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} criado com sucesso!\n'.format(nomeArquivo))

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo,'at')
    except:
        print('Erro ao abrir o arquivo para gravar')
    else:
        a.write('{} ; {}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
    except:
        print('Erro ao abrir arquivo para listar')
    else:
        print(a.read())
    finally:
        a.close()



#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('+', '-' * 20, '+')
    print('|', ' ' * 7, 'MENU', ' ' * 7, '|')
    print('+', '-' * 20, '+')
    print('1 - Cadastrar \n'
          '2 - Listar jogos \n'
          '3 - Sair')

    op = valida_int('Escolha a opção desejada: ',1,3)
    if op ==1:
        print('Opção de dacastrar novo item selecionada... \n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op ==2:
        print('Opção de listar selecionada... \n')
        listarArquivo(arquivo)

    elif op ==3:
        print('Encerrando o programa...')
        break