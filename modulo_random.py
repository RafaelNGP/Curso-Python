"""
Modulo Random e o que sao modulos?

- em Python, nada mais sao que outros arquivos Python.
    - Todos os arquivos que foram criados ate agora sao considerados modulos.
    - Deixar os programas mais simples e permitir a reutilizacao do codigo.
- Modulo Random -> Possui varias funcoes para geracao de numeros pseudo-aleatorios.

Existem duas formas de se utilizar um modulo ou funcao deste.

Forma 1 - Importando o modulo inteiro. (NAO RECOMENDADO)
    import random

    Ao realizar o import, todas as funcoes, atributos, classes e propriedades que estiverem
    dentro do modulo ficarao disponiveis em memoria.
    Testando no console:
        import random
        numero = random.random()
        numero

Forma 2 - Importando uma funcao especifica do modulo
    Ao realizar a importacao da funcao especifica (random) do modulo random.

        from random import random
        for i in range(10):
        print(random())
"""
from random import random

for i in range(10):
    print(random())

print()

from random import uniform
# Gerar um numero pseudo-aleatorio entre os valores estabelecidos

for i in range(10):
    print(uniform(1, 7))

from random import randint
# Gerando um numero pseudo-aleatorio inteiro

for i in range(6):
    print(randint(1, 60), end=" ")

print()
from random import choice
# mostra um valor aleatorio entre um iteravel.

jogadas = ["Pedra", "Papel", "Tesoura"]
for i in range(3):
    print(choice(jogadas))

from random import shuffle
# Tem a funcao de embaralhar dados.

cartas = ["K", "Q", "J", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(cartas)
shuffle(cartas)
print(cartas.pop())
print(cartas)
