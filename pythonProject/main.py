# Expressões algébricas
#
#a) O somatório dos 5 primeiros números inteiros e positivos:

print('a soma dos primeiros 5 primeiros números inteiros é: ',1+2+3+4+5)

#b) A média entre 23,19 e 31
print('a média dos números 23,19 e 31 é: ',(23+19+31)/3)

#c) O número de vezes que 73 cabe em 403
c = int(403//73)
print('O número 73 cabe {} vezes dentro do número 403'.format(c))

#d) A sobra quando 403 é dividido por 73 [ a sobra que menciona é o resto da divisão usando o MOD]
print('O resto da divisão de 403 por 73 é: ',403%73)  #MOD da operação.

#e) 2 Elevado à 10ª potência
print('2 elevador a décima potencia é: ',2**10)

#f) o valor absoluto da diferença entre 54 e 57
print('o valor absoluto da diferenã entre 54 e 57 é: ', abs(54-57))

#g) o menor valor entre 34,29 e 31
#Forma complicada#
a = 34
e = 29
i = 31
resposta = 1
if a < e and a < i:
    resposta = a
if (e < i) and (e < a):
    resposta = e
if i < a and i < e:
    resposta = i
print('O menor valor entre 34,29 e 31 é {}' .format (resposta))
###############################################################################
#Forma resumida
print('O menor valor entre 34,29 e 31 é: ', (min(34, 29, 31)))

############################################################################

  # Atribuição
print(' ')

#a) Atribuir o valor inteiro 3 à variável a
a = 3
print('a= ', a)
#b) Atribuir o valor 4 à variável b
b = 4
print('b= ', b)
#c) Atribuir à variável c o valor da expressão a*a + b*b
c = (a*a+b*b)
print('o valor de a*a+b*b é {}' .format (c))

#Variaveis String

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print('s1: ',s1,' s2: ',s2,' s3: ',s3)
# Utilizando operadores, crie saídas:
#a) ant bat cod
print(s1,s2,s3)
#b) ant ant ant ant ant ant ant ant ant ant
print((s1 + ' ') * 10)
#c) ant bat bat cod cod cod
print(s1 + (' ' + s2 )* 2 + (' ' + s3) *3)
#d) ant bat ant bat ant bat ant bat ant bat ant bat ant bat
print((s1 + ' ' + s2 + ' ')*7)
#e) batbatcod batbatcod batbatcod batbatcod
print((s2+s2+s3+' ')*5)

###############################################################################################################
# Exercício 1

# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado
#a ele. Calcule e esiba o valor do desconto e o preço final do produto ( exercício da apostila - aula 2 )

produto = float(input('qual valor do seu produto?'))
desconto = float(input('qual % de desconto? (0-100)'))
desconto = abs((desconto - 100)/100)
print('o valor do seu produto com o desconto fica em: ', (produto * desconto))
##### outra forma #######
produto = float(input('qual valor do seu produto?'))
p = float(input('qual % de desconto? (0-100)'))
desconto = produto * (p / 100)
final = produto - desconto
print('o preço do produto é {}. Desconto de {}%'.format(produto,p))
print('o valor do seu produto com o desconto de {} fica em:{}' . format (desconto,final))


#########################
# Exercício 2 #

# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado pelo usuário, assim como
#a quantidade de dias pelo quais o carro foi alugado. Calcule o preço a pagar,sabendo que o carro custa
#R$60 por dia e R$0,15 por KM rodado.

kmtotal = float(input('quantos km foram percorridos?'))
tempo = int(input('quantos dias o carro foi alugado'))
diaria = 60
km = 0.15
valordia = diaria * tempo
valorkm =km * kmtotal
valortotal = valorkm + valordia
print('Foi alugado o carro por {} dias e rodado {} km no total.'.format(tempo,kmtotal))
print('O valor total a ser pago é de R${}, sendo total de diária {}R$ e Kilometragem R${}.'.format(valortotal,valordia,valorkm))

##########################################################################################################33

#   Exercício 3

frase = input('Escreva uma frase qualquer')
metade = (len(frase))
frasemeia = frase[:int(metade/2)]
print(frasemeia[-2:])
