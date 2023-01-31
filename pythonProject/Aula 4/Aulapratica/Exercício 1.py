#Escreva um algoritmo que leia dois valores numéricos e pergunte ao usuário qual operação ele deseja realizar
#adição (+), multiplicação (*), subtração (-), divisão (/) e sair. Exiba na tela o resultado da operação
# - Repita até que a opção saída seja escolhida


while True:
    print('CALCULADORA')
    print('Escreva a operação desejada')
    print('adição (+)')
    print('subtração (-)')
    print('multiplicação (*)')
    print('divisão (/)')
    print('ou digite "sair" para finalizar...')
    operador = input('Escolha a opção desejada: ')
    if operador == 'sair':
        print('Finalizando...')
        break
    if operador != '+' and operador != '-' and operador != '*' and operador != '/':
        print('Opção invalida, tente novamente!')
        continue
    x = float(input("digite oprimeiro número da operação: "))
    y = float(input("digite segundo número da operação: "))
    if operador == "+":
        print('{} + {} = {}'.format(x,y,x + y))

    elif operador == "-":
        print('{} + {} = {}'.format(x,y,x - y))

    elif operador == "*":
        print('{} x {} = {}'.format(x,y,x * y))

    elif operador == "/":
        print('{} : {} = {}'.format(x,y,x / y))

    continue




