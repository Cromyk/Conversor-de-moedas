#Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
#Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$100, R$50, R$20, R$10, R$2 e R$1

valor = int(input('Insira o valor desejado para contagem de cédulas'))
contador = valor
c100 = 0
c50 = 0
c20 = 0
c10 = 0
c2 = 0
c1 = 0
if valor >= 100:
    while (contador >= 100):
        c100 += 1
        contador - 100
elif contador >= 50:
    while (contador >= 50):
        c50 += 1
        contador -50
elif contador >= 20 :
    while contador >= 20 :
        c20 += 1
        contador -20
elif contador >= 10:
    while contador >= 10:
        c10 += 1
        contador - 10
elif contador >= 2:
    while contador >= 2:
        c2 += 1
        contador -2
elif contador >= 1:
    while contador >= 1:
        c1 += 1
        contador -1
if c100 > 0:
    print('{} notas de R$100'.format(c100))
if c50 > 0:
    print('{} notas de R$50'.format(c50))
if c20 > 0:
    print('{} notas de R$20'.format(c20))
if c10 > 0:
    print('{} notas de R$10'.format(c10))
if c2 > 0:
    print('{} notas de R$2'.format(c2))
if c1 > 0:
    print('{} notas de R$1'.format(c1))