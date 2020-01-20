"""
Listas Aninhadas (Nested lists)

Algumas linguagens de programacao possuem uma estrutura de dados chamadas de arrays: (C/Java/PHP)
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python, nos temos somente as listas.
numeros = [1, 2, 3, 4, 5] <-- Em java eh um Array, em Python eh uma lista.
mumeros = [1, 1.4, True, "True"]
"""
# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)
print(type(listas))

# Acessando os dados.
print(listas[0])
print(listas[0][1])
print(listas[2][1])
print(listas[-1][-2])

# Iterando com loops com uma lista aninhada
for lista in listas:
    for valor in lista:
        print(valor)

# Iterando com list comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro/matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
