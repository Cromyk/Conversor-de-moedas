#Escreva um altoritmo que lê um nome e uma idade

# Caso o nome digitado seja Vinicius, escreva isso na tela.
# Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos, informe que é de menor.
#Se for maior que 100 anos, informe que esta pessoas possivelmente não existe.

nome = input('Digite um nome: ')
idade = int(input('Digite uma idade'))
if (nome == 'Vinicius'):
    print('{},{} anos.'.format(nome, idade))
elif (idade < 18):
    print('É menor de idade!')
elif (idade > 100):
    print('Esta pessoa possivelmente não existe')