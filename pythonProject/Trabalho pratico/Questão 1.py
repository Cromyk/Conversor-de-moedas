#Programa Inicial

# Menu
print('+','-'*49,'+')
print('| Bem vindo a loja de: Marco Antônio de Souza Matos |')# RU: 4316762
print('+','-'*49,'+')

'''Quantidade	Custo de embalagem para frete:
0 <= quantidade < 11	R$ 30.00            #>= 0 
11 <= quantidade < 101	R$ 60.00            #>= 11  
101 <= quantidade < 1001	R$ 120.00       #>= 101
quantidade >= 1001	R$ 240.00'''

# Coleta de dados de valor e quantidade par acalculos
valor = float(input('Insira o valor do produto: '))
qnt = int(input('Insira a quantidade doproduto: '))
#Multipla resolução para diferentes valores de frete conforme quantidade
# ( passivel de implementação futura, teste para quantidade ser número inteiro e maior ou igual a 0 )
if qnt >= 0 and qnt < 11:  #para valores de 0 a 10
    total = valor * qnt
    frete = total + 30
elif qnt >= 11 and qnt < 101: #para valores de 11 a 100
    total = valor * qnt
    frete = total + 60
elif qnt >= 101 and qnt < 1001: #para valores de 101 a 1000
    total = valor * qnt
    frete = total + 120
else: #para valores diferentes, ou seja, maior ou igual a 1001 (qnt <= 1001)
    total = valor * qnt
    frete = total + 240
# Imprime resultado e encerra o programa.
print('O valor total sem frete foi: R$ %.2f' % total) # mostra saida com apenas 2 digitos na casa decimal
print('O valor total sem frete foi: R$ %.2f . (frete de R$ %.2f)' % (frete,frete-total)) # encontra valor do frete