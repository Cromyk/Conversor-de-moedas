#traduza as afirmações a seguir para condicionais em Python:

#a) Se idade é maior que 60, escreva: "Você tem direitos aos benefícios"

#b) Se dano é maior do que 10 e escudo é igual a 0, escreva: 'Você está morto!'

#c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em true, escreva: "Você escapou!"



#a)
idade = int(input('Qual sua idade? '))
if idade > 60 :
    print('Você tem direitos aos beneficios')

#b)
dano = int(input('Escreva o valor do dano: '))
escudo= int(input('Escreva o valor do escudo: '))
if dano > 10 and escudo == 0 :
    print('Você está morto!')

#c)
norte = input('Você está no norte? sim ou não')
sul = input('Você está no sul? sim ou não')
leste = input('Você está no leste? sim ou não')
oeste = input('Você está no oeste? sim ou não')
if norte == ('sim'):
    norte = True
elif norte == 'não':
    norte = False
elif sul == ('sim'):
    sul = True
elif sul == 'não':
    sul = False
elif leste == ('sim'):
    leste = True
elif leste == 'não':
    leste = False
elif oeste == ('sim'):
    oeste = True
elif oeste == 'não':
    oeste = False

else:
    print('Responda "sim" ou "não"')
if (norte or sul or leste or oeste):
    print("Você escapou!")