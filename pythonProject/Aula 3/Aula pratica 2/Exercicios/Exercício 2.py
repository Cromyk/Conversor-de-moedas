#Escreva um altoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
# Adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada.
print('CALCULADORA')
print('Escolha dentre as opções abaixo:')
print('Adição (+)')
print('subtração (-)')
print('multiplicação (*)')
print('divisão (/)')
print('Pressione outra tecla para sair')
operacao = input('introduza o simbolo de sua escolha: ')
if (operacao != '+') and (operacao != '-') and (operacao != '/') and (operacao != '*'):
    print('Escolheu sair')
else:
    x= int(input('Insira o primeiro número: '))
    y= int(input('Insira o segundo número: '))


    if operacao == '+':
        res = x + y
        print('{} + {} ={}'.format(x,y,res))
    elif operacao == '-':
        res = x - y
        print('{} - {} ={}'.format(x, y, res))
    elif operacao == '*':
        res = x * y
        print('{} x {} ={}'.format(x, y, res))
    elif operacao == '/':
        res = x / y
        print('{} : {} ={}'.format(x, y, res))
print('Encerrando o programa...')



