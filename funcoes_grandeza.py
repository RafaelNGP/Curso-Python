"""
Funcoes de maior grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programacao suporta HOF indica que podemos ter funcoes que retornam outras funcoes
como resultado ou mesmo que podemos passar funcoes como argumentos para outras funcoes e ate mesmo criar
variaveis do tipo funcao para nossos programas.

OBS: Na sessao de funcoes ja utilizamos isso.

Em Python, as funcoes sao cidadoes de primeira classe (First Class Citizen)
"""
from random import choice


# Exemplo - Definindo as funcoes
def somar(a, b):
    return a+b


def diminuir(a, b):
    return a-b


def multiplicar(a, b):
    return a*b


def dividir(a, b):
    return a/b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# testando as funcoes
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


# Nested Functions ou Inner Functions
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de vc '))
    return humor() + pessoa


print(cumprimento('Rafael'))


# retornando funcoes de outras funcoes
def faz_me_rir():
    def rir():
        return choice(('hahahahaha', 'AUHAUHAUAHUA', 'KKKKKKKKKK', 'lol'))
    return rir


# testando
rindo = faz_me_rir()
print(rindo())


# Inner Functions podem acessar o escopo de funcoes externas
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'lol', 'UAHAUHAUHAA', 'hue'))
        return f'{risada} {pessoa}'
    return dando_risada


# testando
rindo = faz_me_rir_novamente('fernanda')
print(rindo())
print(rindo())
print(rindo())
