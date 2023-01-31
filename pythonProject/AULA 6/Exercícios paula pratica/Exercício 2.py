#crie um jogo de pedra papel ou tesoura (Jokenpô). Você deverá jogar contra o computador. Voce irá sempre
#escolher uma das opções: 1- pedra, 2 - papel, 3 - tesoura.

#o computador irá sempre sortear um número de 1 até 3 para jogar
#armazene todos os resultados em uma lista e no final apresente o vencedor

#encerre o programa ao digitar zero
#imput de função:

from random import randint

#Programa principal
placar = []
print('+','-' * 31,'+')
print('|','-' * 7,'Jokenpô machine','-' * 7,'|')
print('+','-' * 31,'+')
print('1 - Pedra\n'
      '2 - Papel\n'
      '3 - Tesoura\n'
      '0 - SAIR')
jogadas= ['Pedra','Papel','Tesoura']
placar = []
while True:
    try:
        player = int(input('Insira sua jogada: '))
    except:
        print('Nao foi possivel reconheccer. insire um número de 0 a 3')
    else:
        pc = randint(1,3)
        if player == 1:
            print('Jogador escolheu {}!'.format(jogadas[player - 1]))
            print('Computador escolheu:{}'.format(jogadas[pc - 1]))
            if pc == player:
                print('Empate')
                placar.append('E')
                continue
            elif pc == 2:
                print('ganhador: Computador')
                placar.append('C')
                continue
            else:
                print('ganhador: Jogador')
                placar.append('J')
                continue


        elif player == 2:
            print('Jogador escolheu {}!'.format(jogadas[player-1]))
            print('Computador escolheu:{}'.format(jogadas[pc-1]))
            if pc == player:
                print('Empate')
                placar.append('E')
                continue
            elif pc == 3:
                print('ganhador: Computador')
                placar.append('C')
                continue
            else:
                print('ganhador: Jogador')
                placar.append('J')
                continue


        elif player == 3:
            print('Jogador escolheu {}!'.format(jogadas[player-1]))
            print('Computador escolheu:{}'.format(jogadas[pc-1]))
            if pc == player:
                print('Empate')
                placar.append('E')
                continue
            elif pc == 1:
                print('ganhador: Computador')
                placar.append('C')
                continue
            else:
                print('ganhador: Jogador')
                placar.append('J')
                continue


        elif player == 0:
            print('Você escolheu sair...')
            break
        else:
            print('insira um número de 1 a 3 para jogar e 0 para sair')

print('O placar ficou em {} para o jogador e {} para o computador e {} Empate(s)'.format(placar.count('J'),placar.count('C'),placar.count('E')))
if placar.count('J') > placar.count('C'): print('Parabens! Você venceu!')
elif placar.count('J') == placar.count('C'): print('Empate!')
else: print('O computador venceu! melhor sorte na proxima vez')