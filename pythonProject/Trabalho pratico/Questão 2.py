#Programa Inicial


#Menu informativo
print('+','-'*55,'+')
print('| Bem vindo a sorveteria de: Marco Antônio de Souza Matos |')# RU: 4316762
print('+','-'*55,'+')
print('')
print(' ','_'*94)
print('| Código |     Descrição      |  Tamanho P (500 ml) | Tamanho M (1000 ml) | Tamanho G (2000 ml) |')
print(' ','_'*94)
print('|   TR   |Sabores tradicionais|        R$6,00       |        R$10,00      |       R$18,00       |')
print('|   ES   |Sabores Especiais   |        R$7,00       |        R$12,00      |       R$21,00       |')
print('|   PR   |Sabores Premium     |        R$8,00       |        R$14,00      |       R$24,00       |')
print(' ','_'*94)

# Iniciar loop de repetição até que finalize
soma = 0
while True:
    tamanho = input('Escolha o tamanho do sorvete ( P/M/G ): ') #tamanho recebe string do tamanho informado no menu
    tamanho = tamanho.upper()
    sabor = input('Escolha o sabor ( TR/ES/PR ): ') #sabor recebe strign do sabor do menu
    sabor = sabor.upper()

# Multipla escolha conforme enunciado, solicitar tamanho e sabor, e informar no final se tem codigo ou tamanho invalido
    # EXIGÊNCIA 1
    # Multipla escolha do tamanho P
    if tamanho == "P":  # para escolha de tamanho Pequeno
        #multipla escolha do sabor, entre TR/ES/PR, caso não for estes sabores ele reinicia
        if sabor == 'TR': # para escolha do sabor tradicional
            soma = soma + 6 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor TRADICIONAL {} de R$6,00'.format(tamanho.upper()))
            print('-'*70) # espaçamento estético no console
        elif sabor == 'ES': # para escolha do sabor especial
            soma = soma +7 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor ESPECIAL {} de R$7,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console
        elif sabor == 'PR': # para escolha do sabor premium
            soma = soma +8 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor PREMIUM {} de R$8,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console

        else: #caso o sabor não esteja dentro dos tipos disponiveis, executa codigo abaixo
            print('!!!!!!!Tamanho ou código invalido(s)!!!!!!!')
            continue

    # EXIGÊNCIA 1
    # Multipla escolha do tamanho M
    elif tamanho == "M":
        #multipla escolha do sabor, entre TR/ES/PR, caso não for estes sabores ele reinicia
        if sabor == 'TR':# para escolha do sabor tradicional
            soma = soma + 10 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor TRADICIONAL {} de R$10,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console
        elif sabor == 'ES':# para escolha do sabor especial
            soma = soma + 12 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor ESPECIAL {} de R$12,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console
        elif sabor == 'PR':# para escolha do sabor premium
            soma = soma + 14 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor PREMIUM {} de R$14,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console

        else: #caso o sabor não esteja dentro dos tipos disponiveis, executa codigo abaixo
            print('!!!!!!!Tamanho ou código invalido(s)!!!!!!!')
            continue# EXIGÊNCIA 2 e 3

#EXIGÊNCIA 1
    # Multipla escolha do tamanho G
    elif tamanho == "G":
        # multipla escolha do sabor, entre TR/ES/PR, caso não for estes sabores ele reinicia
        if sabor == 'TR':# para escolha do sabor tradicional
            soma = soma + 18 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor TRADICIONAL {} de R$18,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console
        elif sabor == 'ES':# para escolha do sabor especial
            soma = soma + 21 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor ESPECIAL {} de R$21,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console
        elif sabor == 'PR':# para escolha do sabor premium
            soma = soma + 24 # Soma é o acumulador que incorporao valor de cara item para somatorio final
            print('Você pediu um sorvete sabor PREMIUM {} de R$24,00'.format(tamanho.upper()))
            print('-' * 70)# espaçamento estético no console

        else: #caso o sabor não esteja dentro dos tipos disponiveis, executa codigo abaixo
            print('!!!!!!!Tamanho ou código invalido(s)!!!!!!!')
            continue# EXIGÊNCIA 2 e 3


    #Caso não esteja dentro da multipla escolha, ele não é invalido.
    else:
        print('!!!!!!!Tamanho ou código invalido(s)!!!!!!!')
        continue# EXIGÊNCIA 2 e 3

   #Repetição se o cliente deseja mais alguma coisa
    rep = input('Deseja pedir mais alguma coisa? ( S/N ) ')
    while rep.upper() not in 'SN':
        print('Desculpe, não entendi, escreva S ou N')
        rep = input('Deseja pedir mais alguma coisa? S para sim e N para não: ')
    if rep.upper() == 'N':
        break   # EXIGÊNCIA 3
    else: continue # EXIGÊNCIA 3
print('Pedido finalizado, o valor total R$ %.2f' % soma)  # Finalização do programa e imprime o acumulador soma
