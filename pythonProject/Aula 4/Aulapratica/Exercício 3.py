#um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se a pessoa tiver menos que
#3 anos de idade, o ingresso será gratuito, se tiver entre 3 e 12 anos, o ingresso custará R$15, se tiver mais de
#12 anos, custará R$30.

#escreva um laço que você pergunte a idade aos usuários e então, informe-lhes o preço do ingresso do cinema.
#encerre o laõ usando um break quando o usuário digitar sair.
#após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro arrecadado
#e a média de idade das pessoas.

print('sistema de contagem de ingressos de cinema:')
print('insira a idade ou digite sair para encerrar: ')
contador = 0
soma = 0
idadetotal =0
while True:
    idade = input('Qual sua idade? ')
    if (idade == 'sair'):
        print('Total de pessoas: {}'.format(contador))
        print('total de dinheiro arrecadado: R${}.'.format(soma))
        print('A média de idade das pessoas é de :{}'.format(idadetotal / contador))
        break
    idade = int(idade)
    contador +=1
    idadetotal += idade
    if (idade >= 3) and (idade <= 12) :
        soma += 15
    if (idade > 12):
        soma = soma + 30
