"""
Dicionarios

Em algumas linguagens de programacao, os dicionarios sao conhecidos como mapas.

Dicionarios sao:
    - colecoes do tipo chave/valor
    - representados por chaves {}
    - class <dict>
    - 'chave': 'valor'
    - Pode ser de qualquer tipo de dado.
"""

paises = {'br': 'Brasil', 'us': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# Forma recomendada (encontrei fucando)
print(paises.get('br'))
print(paises.get('ru'))
print(paises.get('py'))
