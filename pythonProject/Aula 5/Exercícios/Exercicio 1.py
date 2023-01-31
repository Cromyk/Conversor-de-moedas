#Escreva uma função que calcule o fatorial de um número recebido como parâmetro e retorne o seu resultado
#faça uma validação dos dados por meio de uma outra função, permitindo que somente valores positivos sejam aceitos
#crie o help da sua função ( Exercício da apostila)

def fatorial(x):
    """
    Função que faz a fatoração do número inteiro inserido.
    Validação do valor inserido, caso negativo retorna com frase "Número negativo! invalido".
    Caso validação positiva, retorna valor
    :param x: Valor inteiro obrigatorio
    :return: se validação TRUE , retorna resultado da fatoração
    :return: se validação FALSE, retorna "Número negativo! invalido"
    """
    if vali_neg(x):
        if x == 0:
            return 1
        else:
            res = 1
            for i in range(1,x + 1):
                res *= i
            return res
    else:
        return 'Número negativo! invalido'

def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
        except ValueError:
            print('você não digitou um número')
            continue
        else:
            break
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vali_neg(x):
    """
    Função de validação se o valor informado é negativo
    :param x: Valor inteiro obrigatório
    :return: False para valores negativos e True para valores positivos
    """
    if x < 0:
        return False
    else:
        return True


# Programa Principal


numero = valida_int('Insira um número entre 0 e 100 para fatorar: ',0,100)
print('{}! = {}'.format(numero , fatorial(numero)))




