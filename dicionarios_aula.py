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

russia = paises.get('ru', 'Nao encontrado')
# primeiro valor para verdadeiro, segundo para caso falso

if russia:
    print("Encontrei o Pais!")
else:
    print("Ainda n foi adicionado")
#
print()
# Verificando se as chaves sao encontradas no dicionario
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

print()
# Podemos utilizar qualquer tipo de dado (int, float, str, boolean), inclusive listas, tuplas, dicionarios etc...
localidades = {
    (35.6895, 39.6917): "Escritorio em Tokyo",
    (40.7128, 74.0060): "Escritorio em Nova York",
    (35.7749, 122.4194): "Escritorio em Sao Paulo"
}
print(localidades)
print(type(localidades))
print()
# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# forma 1
receita['abr'] = 350
print(receita)
#
print()
# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionario
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)
# A forma de adicionar novos elementos ou atualizar dados em um dicionario eh a mesma.
# Em dicionarios, nao podemos ter chaves repetidas.

# Remover dados de um dicionario
# Forma 1
print(f'Elemento removido: {receita.pop("mar")}')
print(receita)

# Forma 2
del receita['fev']
print(receita)
print()
#
# carrinho = []
# produto1 = ['Playstation 4', 1, 230.00]
# produto2 = ['God of War 4', 1, 150.00]
# carrinho.append(produto1)
# carrinho.append(produto2)
# print(carrinho)
#
carrinho = []
produto1 = {"nome": "Playstation 4", "quantidade": 1, "preco": 2300.00}
produto2 = {"nome": "God of War 4", "quantidade": 1, "preco": 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
