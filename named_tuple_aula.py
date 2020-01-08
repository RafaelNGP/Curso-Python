"""
Modulo Collections - named tuple

Named Tuple -> Sao tuplas diferenciadas onde especificamos para ela e tambem parametros.
"""
# Recap tupla
tupla = 1, 2, 3
print(tupla)
print(tupla[1])
print(type(tupla))

# Importando
from collections import namedtuple

# Precisamos definir o nome e parametros
# Forma 1
cachorro = namedtuple('cachorro', 'idade' 'raca' 'nome')

# Formq 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade=2, raca="Pastor", nome="Raymundo")
snow = cachorro(idade=9, raca="Tomba-Lata", nome="Snow")
print(ray)

# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

# Minha forma
elementos = 0
while elementos < len(ray):
    print(ray[elementos])
    elementos += 1

print(snow)
