"""
Sorted

As mudancas que acontecem em uma lista/tupla usando o Sorted nao sao permantente, apenas sao visiveis
no momento em que foi chamado. O valor da variavel nao eh modificado.
"""
lista = [6, 1, 8, 2]
print(lista)
print(sorted(lista))
print(sorted(lista, reverse=True))

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos!", "Eu adoro Pizza!"]},
    {"username": "manuel", "tweets": ["@samuel quem gosta de bolo eh cuzao!", "@samuel gado demais"]},
    {"username": "gabriel", "tweets": ["@samuel Eu adoro bolos! #teambolo"]},
    {"username": "palominha", "tweets": []},
    {"username": "guimanuel", "tweets": ["@palominha Oi gata"]},
    {"username": "rafael", "tweets": ["@guimanuel aff gado d+++", "Eu adoro burger!", "Pizza <3"]}
]
print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario['username']))
