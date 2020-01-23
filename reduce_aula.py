"""
Reduce

OBS: A partir do Python3+ a funcao reduce() nao eh mais uma funcao integrada (built-in)
Agora precisamos importa-la a partir do modulo 'functools'

Guido van Rossum: utilize a funcao reduce() se voce realmente precisa dela, em 99% das vezes um
loop for eh mais legivel.

Para entender o reduce()
Imagine que voce tem uma colecao de dados
    dados = [a1, a2, a3 ... an]

e voce tem uma funcao que recebe dois parametros
    def funcao(x, y):
        return x * y

Assim como map() e filter(), a funcao reduce() recebe dois parametros:
    reduce(funcao, dados)

A funcao reduce() funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) - Aplica a funcao nos dois primeiros elementos da colecao e guarda     o resultado.
    passo 2: res2 = f(res1, a3) - Aplica a funcao passando o resultado do passo1 + o terceiro elemento     e quarda o resultado.
    passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a funcao passando como primeiro argumento o resultado da aplicacao
anterior. No final, reduce() ira retornar o resultado final.

Alternativamente, poderiamos ver a funcao reduce() como:
    funcao(funcao(funcao(a1, a2), a3), a4), ... an)
"""
from functools import reduce

# Vamos utilizar a funcao reduce() para multiplicar todos os numeros de uma lista.
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
print(reduce(lambda x, y: x * y, dados))

# Utilizando um loop for
res = 1
for numero in dados:
    res *= numero
print(res)
