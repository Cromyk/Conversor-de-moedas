#Escreva um algoritmo que cria uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada palavra.
#Faça um print na tela com o nome da palavra e suas respectivas vogais.
#Vogais = a e i o u

#programa principal

palavras = ('arroz','feijao','abacate','machado','mochila','agua','bacon','camisa','caderno','lapis')

for palavra in palavras:
    print('\n Palavra: {} . Vogais: '.format(palavra.upper()), end='')
    for letras in palavra:
            if letras.lower() in 'aeiou':
               print(letras.upper(), end=' ')

