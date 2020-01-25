"""
Zip

zip() - Cria um iteravel (zip object) que agrega elementos de cada um dos iteraveis passadas como
entrada em pares.
"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionario
zip1 = zip(lista1, lista2)
print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# O zip utiliza como parametro o menor tamanho em iteravel, isso significa que se estiver trabalhando
# com iteraveis de tamanho diferentes, ira parar quando os elementos do menor iteravel acabarem.
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos usar diferentes iteraveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dici = {'a': 11, 'b': 12, 'c': True, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dici.values())
print(list(zt))

dados = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
print(list(zip(*dados)))

# Mais complexo
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

