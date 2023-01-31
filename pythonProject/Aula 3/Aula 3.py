# Desenvolva um programa que lê dois valores numéricos inteiros e compara se o primeiro é maior que o segundo,
#utilizando uma condiçional simples

#Caso seja ( resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor digitado
#é maior do que o segundo

x = float(input('Digite o primeiro valor numérico'))
y = float(input('Digite o segundo valor numérico'))
if (x > y):
    print('o valor do primeiro número é maior que o segundo : {}'.format(x))

###################################################################
# not #
a = True
b = False
print(not a)
print(not b)

######################################################
# and #
a = True
b = False
print(a and b)

#######################################################
# or
a = True
b = False
print(a or b)
#######################################