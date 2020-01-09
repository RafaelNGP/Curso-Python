"""
Funcoes com retorno

PS: Pulei a explicacao demorada e fiz minha propria funcao com retorno "quadrado_numero", eh possivel
incrementar ela dando um metodo input.

Sobre a palavra reservada return:
    - Ela finaliza a funcao, ou seja, ela sai da execucao da funcao
    - Podemos ter, em uma funcao, diferentes returns
    - Podemos, em uma funcao, retornar qualquer tipo de valor e ate mesmo multiplos valores.
"""
from random import random


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


def quadrado_numero(x):
    return x ** 2


def diz_oi():
    return "oi"


def moeda():
    if random() > 0.5:
        return "Cara!"
    return "Coroa!"


# Demonstrando o que eh retorno
numeros = [1, 2, 3]
ret_pop = numeros.pop()
ret_prt = print(numeros)

print(f'Retorno de pop: {ret_pop}\n'
      f'Retorno de print: {ret_prt}')

# Minha funcao
print(quadrado_numero(7))
print(quadrado_numero(5))

# Exemplo do curso
print(diz_oi())
print(nova_funcao())


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
print(outra_funcao())

print(type(num1))
print(type(outra_funcao()))

print(moeda())


def soma_impares(base):
    total = 0
    for numero in base:
        if numero % 2 != 0:
            print(f'Valor total: {total} + {numero}')
            total += numero
    return total


n = int(input("Com o limite? "))
valor_base = range(n)
print(soma_impares(valor_base))
