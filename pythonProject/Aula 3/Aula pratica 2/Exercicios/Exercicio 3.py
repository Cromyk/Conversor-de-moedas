#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencial ,I para industrial e C para comércios

#R = até 500 R$0,4  | acima de 500 R$0,65
#I = até 5000 R$0,55  | acima de 5000 R$0,60
#C = até 100 R$0,55  | acima de 500 R$0,60

print('CACULADORA DE CONSUMO ELÉTRICO')
print('Selecione o tipo de estabelecimento:')
print('r - Residencial')
print('c - Comercial')
print('i - Industrial')
print('Pressione qualquer outra tecla para sair...')
tipo = input('Selecione o tipo desejado: ')
if tipo == 'r' or tipo == 'c' or tipo =='i':
    consumo = float(input('Digite o consumo em kWh: '))
    if tipo == 'r':
        if consumo <= 500:
            soma = consumo * 0.4
            print('RESIDENCIAL- o valor da energia elétrica é de R${}.'.format(soma))
        else:
            soma = consumo * 0.65
            print('RESIDENCIAL- o valor da energia elétrica é de R${}.'.format(soma))
    elif tipo == 'c':
        if consumo <= 1000:
            soma = consumo * 0.55
            print('COMERCIAL- o valor da energia elétrica é de R${}.'.format(soma))
        else:
            soma = consumo * 0.60
            print('COMERCIAL- o valor da energia elétrica é de R${}.'.format(soma))
    elif tipo == 'i':
        if consumo <= 5000:
            soma = consumo * 0.55
            print('INDUSTRIAL- o valor da energia elétrica é de R${}.'.format(soma))
        else:
            soma = consumo * 0.60
            print('INDUSTRIAL- o valor da energia elétrica é de R${}.'.format(soma))

else:
    print('Encerrando calculadora...')