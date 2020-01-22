"""
Filter

filter() -> Serve para filtrar dados de uma determinada colecao.
"""
import statistics

valores = 1, 2, 3, 4, 5, 6
media = (sum(valores) / len(valores))
print(media)

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a funcao mean()
media = statistics.mean(dados)
print(media)

res = filter(lambda x: x > media, dados)
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', ' ']
filtrando = filter(None, paises)
print(list(filtrando))

# Exemplo proprio (mais trabalhoso)
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', ' ']
paises_filtrados = []
for items in paises:
    if items != '':
        paises_filtrados.append(items)

print(paises_filtrados)

# Exemplo mais complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos!", "Eu adoro Pizza!"]},
    {"username": "manuel", "tweets": ["@samuel quem gosta de bolo eh cuzao!", "@samuel gado demais"]},
    {"username": "gabriel", "tweets": ["@samuel Eu adoro bolos! #teambolo"]},
    {"username": "palominha", "tweets": []},
    {"username": "guimanuel", "tweets": ["@palominha Oi gata"]},
    {"username": "rafael", "tweets": ["@guimanuel aff gado d+++", "Eu adoro burger!", "Pizza <3"]}
]

# Filtrar os usuarios que estao inativos no twitter
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Forma 2 de fazer a filtragem
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)

# Como combinar filter() e map()
# Devemos criar uma lista contento 'Sua instrutora eh: <nome>' desde que cada nome tenha menos de 5 caracteres
# Minha forma
nomes = ['Vanessa', 'Ana', 'Maria']
lista = filter(None, (map(lambda nome: f'Sua instrutora eh: {nome}' if len(nome) < 5 else None, nomes)))
print(list(lista))

# Forma da aula
nomes = ['Vanessa', 'Ana', 'Maria']
lista = list(map(lambda nome: f'Sua instrutora eh: {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
