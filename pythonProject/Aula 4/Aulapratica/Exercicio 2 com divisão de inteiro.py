# Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
# Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$100, R$50, R$20, R$10, R$2 e R$1

valor = int(input('Insira o valor desejado para contagem de cédulas: '))
while True:
    if valor >= 100:
        c100 = valor // 100
        print('{} cédulas de R$100'.format(c100))
        valor -= (c100 * 100)
        if not valor:
            break
    if valor >= 50:
        c50 = valor // 50
        print('{} cédulas de R$50'.format(c50))
        valor -= (c50 * 50)
        if not valor:
            break
    if valor >= 20:
        c20 = valor // 20
        print('{} cédulas de R$20'.format(c20))
        valor -= (c20 * 20)
        if not valor:
            break
    if valor >= 10:
        c10 = valor // 10
        print('{} cédulas de R$10'.format(c10))
        valor -= (c10 * 10)
        if not valor:
            break
    if valor >= 2:
        c2 = valor // 2
        print('{} cédulas de R$2'.format(c2))
        valor -= (c2 * 2)
        if not valor:
            break
    if valor:
        c1 = valor
        print('{} cédulas de R$1'.format(c1))
        break

