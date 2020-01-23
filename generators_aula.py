"""
Generators

Comparado ao List, Dict e Set Comprehension, o generator usa MUITO MENOS memoria.
"""
nomes = ['Carla', 'Carolina', 'Camila']

# Ex 1
print(any(nome[0] == 'C' for nome in nomes))

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

