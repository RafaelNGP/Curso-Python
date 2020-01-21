"""
Map (nao eh igual ao arquivo mapas_aula)

Com map fazemos mapeamento de valores para funcao.
"""
import math


def area(r):
    """Calcula a area de um circulo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
# Forma comum
areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 - Usando maps
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Exemplo proprio
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Apos utilizar a funcao map() depois da primeira utilizacao do resultado, ele zera.