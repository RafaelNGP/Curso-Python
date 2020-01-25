"""
Min e Max

max() - Retorna o maior valor em um iteravel ou o maior de dois ou mais elementos.
min() - Retorna o menor item em um iteravel ou o menor de dois ou mais elementos.
"""
# Exemplos
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))
print(max(dicionario.values()))

print(max(3, 34))

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

# Desafio: Imprimir somente o titulo da musica mais e menos tocada.
musicas = [
    {'Titulo': 'Eye of the Storm', 'tocou': 30},
    {'Titulo': 'The last Fight', 'tocou': 25},
    {'Titulo': 'Alone', 'tocou': 40},
    {'Titulo': 'Waking the Demon', 'tocou': 22}
]

print(max(musicas, key=lambda musica: musica["tocou"]).get("Titulo"))
print(min(musicas, key=lambda musica: musica["tocou"]).get("Titulo"))
