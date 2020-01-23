"""
Any e All

all() = retorna True se todos os elementos do iteravel sao verdadeiros ou ainda se o iteravel esta vazio
any() = retorna True se qualquer elemento do iteravel for verdadeiro, se o iteravel estiver vazio, eh false.
"""

# Ex all
print(all([1, 2, 3, 4]))        # True
print(all([0, 1, 2, 3, 4]))     # False
print(all([]))                  # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print(all([letra for letra in 'eio' if letra in 'aeiou']))
print(all(numero for numero in [4, 2, 10, 6, 8] if numero % 2 == 0))

# Ex any
print(any([0, 1, 2, 3, 4]))
print(any([0]))
print(any([None, False, 0, 1]))

