# um aluno, para passar de ano precisa ser aprovado em todas as matérias que estácursando.

# Assuma que a média para aprovação é a partir de 9, e que o aluno cursa 3 matérias, somente.
#escreva um algoritmo que leia a nota final do aluno em cada matéria e informe , na tela se ele passou de ano ou não

d1 = float(input('Qual sua nota final da matéria 1 :'))
d2 = float(input('Qual sua nota final da matéria 2 :'))
d3 = float(input('Qual sua nota final da matéria 3 :'))
if (d1 >= 7) and (d2 >= 7) and (d3 >= 7):
    print('Parabens! você foi aprovado em todas as matérias')
else :
    print('Que pena,você não foi parovado em todas as matérias')