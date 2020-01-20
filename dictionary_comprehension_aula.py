"""
Dictionary Comprehension

Pensar no seguinte:
Se quisermos criar:
lista = [1, 2, 3, 4]
tupla = 1, 2, 3, 4
conjunto = {1, 2, 3, 4}
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

{chave:valor for valor in iteravel}
"""
# Exemplos
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in dicionario.items()}
print(quadrado)

#
numeros = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

print({chaves[i]: valores[i] for i in range(0, len(chaves))})

# Exemplo com logica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
