# total = (metragem * tipo) + adicional(is)
#Funções:

def metragem_limpeza():
    """
    Função solicita a metragem da limpeza e retorna o valor.
        metragem                Valor
        30 até 299          60+0.3*metragem
        300 até 700         120+0.5*metragem
        outros valores      não são aceitos
    :return: retorna metragem
    """
    while True:
        try:
            tamanho = float(input('Entre com a metragem do local: '))
        except:
            print('Ops! não entendi, insita o m³ do local em números...')
            continue
        else:
            if tamanho >= 30 and tamanho < 700:
                break
            else:
                print('Valor não foi aceito, insira um numero entre 30 e 699')
                continue
    return tamanho

def tipo_limpeza():
    """
    Função que pede e verifica o tipo de limpeza entre os 2 tipos disponiveis:
            TIPO                                                            Multiplicador
            B - Básica- indicada para sujeiras semanais ou quinzenais       1.00
            C- Completa- indicada para sujeiras antigas e/ou não rotineiras 1.3
    :return: retorna o valor do multiplicador
    """
    while True:
        print('B - Básica- indicada para sujeiras semanais ou quinzenais\n'
              'C- Completa- indicada para sujeiras antigas e/ou não rotineiras (30% mais caro)')
        tipo = input('Insira o tipo de alimpeza desejada: ')

        if tipo.upper() == 'B':
            valor = 1
            break
        elif tipo.upper() == 'C':
            valor = 1.3
            break
        else:
            print('!!!TIPO DE LIMPEZA INVALIDO!!!')
            continue
    return valor

def adicional_limpeza() :
    """
    Função pede o adicional para o usuário em loop interativo e retorna o valor total

            Adicionais                                      VALOR
            0 não desejo mais nada                            0,00
            1 passar 10 peças de roupas R$10                  10,00
            2 Limpeza de 1 forno/Micro-ondas R$12            12,00
            3 Limpeza de 1 geladeira/Freezer R$20            20,00

    :return: Retorna o valor total de adicionais
    """
    valor = 0
    while True:
        print('Adicionais                                      VALOR\n'
              '0- não desejo mais nada                      R$0,00\n'
              '1- passar 10 peças de roupas                R$10,00\n'
              '2- Limpeza de 1 forno/Micro-ondas            R$12,00\n'
              '3- Limpeza de 1 geladeira/Freezer            R$20,00')
        try:
            add = int(input('Insira o adicional se desejar, ou insire 0 para encerrar: '))
        except:
            print('Por favor, insira um valor númerico de 0 a 3')
            continue
        else:
             #'0- não desejo mais nada
            if add == 0:
                break
            #'1- passar 10 peças de roupas                  R$10,00
            elif add == 1:
                valor += 10
                continue
            #'2- Limpeza de 1 forno/Micro-ondas            R$12,00
            elif add == 2:
                valor += 12
                continue
            #'3- Limpeza de 1 geladeira/Freezer            R$20,00')
            elif add == 3:
                valor += 20
                continue
            else:
                print('número invalido')
                continue
    return valor #retorna o valor total dos adicionais
###########################################################################################
#Programa inicial

#Menu informativo
print('+','-'*61,'+')
print('| Bem vindo a serviços de limpeza: Marco Antônio de Souza Matos |')# RU: 4316762
print('+','-'*61,'+')
print('')
soma = 0 #cria variavel soma para o algoritmo
#Solicita metragem
print('*'*73)   # Espaçamento estético
print('-'*20,' Menu 1 de 3 - Metragem Limpeza','-'*20)# informação intuitiva para usuário
tamanho = metragem_limpeza()  #armazena valor do retorno na variavel
if tamanho >= 30 and tamanho < 300: # verifica a metragem e atribui o valor calculado na variavel valor
    valor = tamanho * 0.3 + 60

else: # verifica a metragem e atribui o valor calculado na variavel valor
    valor = tamanho * 0.5 + 120
soma += valor #soma no acumulador
#Solicita tipo
print('*' * 73) # Espaçamento estético
print('-'*20,' Menu 2 de 3 - Tipo de Limpeza','-'*21)# informação intuitiva para usuário
tipo = tipo_limpeza()  #armazena valor do retorno na variavel
soma *= tipo #soma no acumulador
#solicita adicional
print('*' * 73) # Espaçamento estético
print('-'*23,' Menu 3 de 3 - Adicional','-'*23)# informação intuitiva para usuário
adicional = adicional_limpeza()  #armazena valor do retorno na variavel
soma += adicional #soma no acumulador
print('*' * 73)# Espaçamento estético
print("Valor total R$ %.2f (metragem: %.2f m³ * tipo: %.2f + aicional: %.2f)" % (soma,tamanho,tipo,adicional))
print('*' * 73)# Espaçamento estético
