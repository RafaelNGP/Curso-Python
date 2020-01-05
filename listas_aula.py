"""
Listas

Funcionam como vetores/matrizes (arrays) com a diferenca de serem dinamicos
e tambem podermos colocar qualquer tipo de dado.

C ou Java: Arrays
    - Possuem tamanho e tipo de dado fixo;

Python
- Dinamico: Nao possui tamanho fixo; ou seja, podemos criar a lista e ir adicionando elementos.
- Qualquer tipo de dado: Nao possuem tipagem de dado, entao qualquer dado pode ser adicionado.

As listas em Python sao representadas por colchetes []
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ["G", "E", "E", "K", "", "U", "N", "I", "V", "E", "R", "S", "I", "T", "Y"]
lista3 = []
lista4 = list(range(11))
lista5 = list("Geek University")

# Podemos checar se determinado valor esta contido na lista
num = 3
if num in lista4:
    print(f"Encontrei o numero {num}")
else:
    print(f"Nao encontrei o numero {num}")

# Podemos ordenar uma lista
lista1.sort()
print(lista1)

# Podemos contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count("e"))
print(f"Numero de ocorrencias do numero 1 na lista1: {lista1.count(1)}")
print(f"Numero de ocorrencias da letra 'e' na lista5: {lista5.count('e')}")

# Adicionar elementos em listas (append)
print(lista1)
lista1.append(42)
print(lista1)

# lista1.append(2, 3, 4)
# Aqui sera adicionada uma lista dentro da lista (sublista)
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print("encontrei o valor")
else:
    print("nao foi encontrado")

# Coloca os elementos da lista dentro da lista
lista1.extend([123, 44, 77])
print(lista1)
