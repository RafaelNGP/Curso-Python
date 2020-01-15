"""
List Comprehension

- Utilizando List Comprehension, nos podemos gerar novas listas com dados processados a partir de
outro iteravel.

# Sintaxe
[ dado for dado in iteravel ]
"""


def quadrado(valor):
    return valor ** 2


# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]

print(res)
"""
Para entender melhor o que esta acontecendo, devemos dividar a expressao em duas partes:
    - A primeira parte: for numero in numeros
    - A segunda parte: numero * 10
"""
res = [quadrado(numero) for numero in numeros]
print(res)
print(len(res))

# List Comprehension VS Loop

# Loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])

# Outros exemplos
# 1
nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2 - Exemplo proprio
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.title() for amigo in amigos])

# 3 - Ja fiz um teste do Range na aula de For
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in numeros])
