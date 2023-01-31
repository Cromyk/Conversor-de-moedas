### Escreva um altoritmo em python em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas.
#Deverá ser apresentado na tela um menu com as opçôes 1 para maça, 2 para laranja e 3 para banana

# após escolhida a fruta, deve-se digitar quantas unidade se quer comprar. O algoritmo deve calcular o preço total
# a pagar do produto escolhido e mostrá-lo  na tela

#considere que uma maça custa R$2,30, uma laranja, R$3,60, e uma banana R$1,85.
print('Escolha o item que deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
fruta = int(input('Digite o numero correspondente a sua escolha: '))
f1 = 2.3
f2 = 3.6
f3 = 1.85
quantidade = int(input('Digite a quantidade de frutas que quer comprar: '))
if (fruta == 1):
  pagar = quantidade * f1
  print('Voce comprou {} maças, o total da sua compra é de R${}'.format(quantidade, pagar))
elif fruta == 2:
    pagar = quantidade * f2
    print('Voce comprou {}  laranas, o total da sua compra é de R${}'.format(quantidade, pagar))
elif fruta == 3:
    pagar = quantidade * f3
    print('Voce comprou {}  bananas, o total da sua compra é de R${}'.format(quantidade, pagar))
else:
     print('Produto inexistente!')