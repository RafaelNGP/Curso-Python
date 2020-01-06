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

# Podemos converter uma string em uma lista
# O Split separa os elementos da lista com o espaco
# Ex 1
curso = "Programacao em Python Essencial"
print(curso)
curso = curso.split()
print(curso)
# Ex 2
print()
curso = "Programacao,em,Python,Essencial"
print(curso)
curso = curso.split(",")
print(curso)

# Convertendo uma lista em String
lista6 = ["Programacao", "Em", "Python", "Essencial"]
curso = ' '.join(lista6)
print(curso)
print()
lista6.clear()

# Iterando sobre listas
# Ex 1
soma = 0
for elemento in lista1:
    soma += elemento
    print(f"Item: {elemento}\nSoma: {soma}")

# Ex 2
carrinho = []
produto = ""

while produto != "sair":
    produto = input("Escolha uma opcao:\nA)Digite o nome de um produto"
                    "\nB)Digite 'carrinho'\n"
                    "C)Digite 'sair'\n").lower()
    if produto == "carrinho":
        print(carrinho)
    else:
        carrinho.append(produto)