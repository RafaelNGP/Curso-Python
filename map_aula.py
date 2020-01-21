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

"""
Para fixar - Map

temos dados iteraveis:
    dados: a1, a2 ... an
    
temos uma funcao:
    funcao: f(x)
    
utilizamos a funcao map(f, dados) onde map ira mapear cada elemento dos dados
e aplicar a funcao.
    O map object: f(a1), f(a2), f(...), f(an)
"""

cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ("Tokyo", 27)]
print(cidades)
# Formula para converter c para f
# f = 9/5 * c + 32

# lambda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

# exemplo proprio - metodo direto
print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
