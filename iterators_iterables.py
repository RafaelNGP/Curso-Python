"""
Diferenca entre Iterable e Iterators

Iterator:
    -> Um objeto que pode ser iterado.
    -> Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() eh chamada.

Iterable:
    -> Um objeto que ira retornar um iterator quando a funcao iter() for chamada.
"""

nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print()
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

print()
for n in numeros:
    print(n)
