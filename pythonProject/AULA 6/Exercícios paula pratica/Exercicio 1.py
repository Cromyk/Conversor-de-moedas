#Escreva um algoritmo que cria uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada palavra.
#Faça um print na tela com o nome da palavra e suas respectivas vogais.
#Vogais = a e i o u

def verificavogal(letra):
    for i in letra:
        i = i.lower
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            p.append(i)

#programa principal

palavras = ('arroz','feijao','abacate','machado','mochila','agua','bacon','camisa','caderno','lapis')
p = []
for palavra in palavras:
    p.clear()
    for letras in palavra:
            if letras.lower() in 'aeiou':
                p.append(letras)

    print('{} = {}'.format(palavra,p,''.join(p)))