#Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:
   # notas = [9,7,7,10,3,9,6,6,2]

    #a) encontrar quantos alunos tiraram nota 7
    #b) Alterar a última nota para 4
    #c) Encontrar a maior nota
    #d) Ordenar a lista de notas
    #e) a média das notas


#Programa principal
notas = [9,7,7,10,3,9,6,6,2]

#a)encontrar quantos alunos tiraram nota 7
print (notas)
print('{} aluno(s) tiraram nota 7'.format(notas.count(7)))

#b) Alterar a última nota para 4
notas[-1] = 4
print(notas)

#c) Encontrar a maior nota
maior_nota = 0
for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
print('A maior nota tirada foi: {}'.format(maior_nota))

#d)Ordenar a lista de notas
print(sorted(notas))
print(sorted(notas,reverse = True))
#e) a média das notas
total = 0
for i in notas:
    total += i
print('Média das notas é de :{}'.format(total / len(notas)))


