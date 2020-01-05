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

# Podemos inserir um novo elemento na lista informando a posicao do indice
lista1.insert(2, "novo valor")
print(lista1)

# POdemos juntar duas listas
lista6 = lista1 + lista2
print(lista6)
# lista1.extend(lista2)
# print(lista1)

# Podemos inverter uma lista
print()
# lista1.reverse()
# lista2.reverse()
print(lista1)
print(lista1[::-1])
print(lista2)
print(lista2[::-1])

# Copiar uma lista
print()
lista6 = lista2.copy()
print(lista6)

# Ver o tamanho de uma lista
print()
print(len(lista1))
print(lista1.__len__())
print(f"Lista1: {len(lista1)}, Lista2: {len(lista2)}, Lista3: {len(lista3)}, Lista4: "
      f"{len(lista4)}, Lista5: {len(lista5)}, Lista6: {len(lista6)}")

# Podemos remover o ultimo elemento de uma lista
# pop retorna o elemento e retira da lista ao mesmo tempo.
print()
lista7 = lista5.copy()
print(lista7)
lista7.pop()
print(lista7)
# Podemos remover um elemento direto por seu indice
lista7.pop(4)
lista7.append("y")
print(lista7)

# Podemos remover todos os elementos (zerar)
print()
lista7.clear()
print(lista7)

# Podemos repetir elementos de uma lista
lista7 = [1, 2, 3]
print(lista7)
print(lista7*3)
