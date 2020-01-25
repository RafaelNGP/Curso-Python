"""
Reversed

Nao confundir com a funcao reverse() das listas.
A funcao do reversed eh inventer um iteravel, nao precisando ser apenas listas.
"""
# Exemplos
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(list(res))
print(type(res))

tupla = 1, 2, 3, 4, 5
res = reversed(tupla)
print(res)
print(tuple(res))
print(type(res))

# Usando reversed na iteracao
for letra in reversed("Geek University"):
    print(letra, end="")

print()
# Fazendo o mesmo sem for.
print(''.join(list(reversed("Geek University"))))
