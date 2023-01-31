#Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
#Verifique se os valores formam um triângulo e classifique como:
# para ser um triangulo nenhum lado pode ser igual a zero, e um lado não pode ser maior que a soma dos outros dois

l1 = int(input('insita o valor do primeiro lado do triangulo: '))
l2 = int(input('insita o valor do segundo lado do triangulo: '))
l3 = int(input('insita o valor do terceiro lado do triangulo: '))

if (l1 == 0 or l2 == 0 or l3 == 0):
    print("isto não é um triangulo")
elif (l1 > l2 + l3) or (l2 > l1 + l3) or (l3 > l1 + l2):
     print("isto não é um triangulo")
elif l1 == l2 and l1 == l3 :
    print('Triangulo Equilátero')
elif (l1 == l2 or l1 == l3) :
    print('Triangulo Isósceles')
else:
    print('Triangulo Escaleno')