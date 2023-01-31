#Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
#Armazene os dados em um dicinário com listas
#Ao encerrar o cadastro, apresente:
 #o total de cadastros efetuados
 #a média das idades das pessoas
 #uma lista de mulheres com menos de 30 anos
 #uma lista de homens com idade acima da média
def idade():
    while True:
        ano = input('Insira o ano de nascimento: ')
        if len(ano)!= 4:
            print('O ano precisa ter 4 digitos... Exemplo: 1991')
            continue
        else:
            ano = int(ano)
            if ano > 2023:
                print('Ops! verifique o ano de nascimento, possivelmente você não naceu ainda')
                continue
            else:
                break
    return ano
def cadastro(lista):

    nome = input('Insira o nome: ')
    ano = idade()

    while True:
        sexo = input('Insira M para masculino ou F para feminimo')
        if sexo.lower() == 'm' or sexo.lower() == 'f':
            break
    lista['nome'].append(nome)
    lista['ano'].append (ano)
    lista['sexo'].append (sexo)

#Programa inicial
print('Cadastro depessoas: ....')
lista = {'nome':[],'ano':[],'sexo':[]}
homens = []
mulheres = []


media = 0
while True:
    print('Você tem {} nomes cadastrados'.format(len(lista['nome'])))
    print('Para um novo cadastro digite "1"\n'
          'Para sair digite "0"')
    try:
        res = int(input(': '))
    except:
        print('Algo inesperado aconteceu, digite apenas 0 ou 1')
        continue
    else:
        if res == 0:
            print('Encerrando o programa...')
            print(lista)
            break
        elif res == 1:
            cadastro(lista)
        else:
            print('Número invalido, digite apenas 0 ou 1')
            continue
media = 0
idadetotal =0
for i in lista['ano']:
    i = int(i)
    idade = 2023 - i
    idadetotal += idade
media = idadetotal / len(lista['ano'])
print('A média das idades cadastradas é de {}'.format(media))
cont = 0
for index in lista['sexo']:
    if index.lower() == 'm':
        if (2023 - int(lista['ano'][cont])) > media:
            homens.append(lista['nome'][cont])
    if index.lower() == 'f':
        if (2023 - int(lista['ano'][cont])) < 30:
            mulheres.append(lista['nome'][cont])
    cont += 1

print('Lista de homens com idade superior a idade média:\n ',' '.join(homens))
print('Lista de mulheres com idade menor que 30 anos:\n ',' '.join(mulheres))