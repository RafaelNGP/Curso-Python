"""
Modulo Collections - Ordered Dict

OrderedDict -> Eh um dicionario, que nos garante a ordem de insercao dos elementos.
"""
from collections import OrderedDict

dicionario = OrderedDict({'a': 200, 'b': 150, 'c': 100})
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")
print(f'\n{dicionario}')

# Entendendo a diferenca entre Dict e Ordered Dict
# Dicionarios normais
dicionario1 = {'a': 200, 'b': 150, 'c': 100}
dicionario2 = {'c': 100, 'b': 150, 'a': 200}
print(dicionario1 == dicionario2) #True

# Ordered Dict
oDict1 = OrderedDict(dicionario1.copy())
oDict2 = OrderedDict(dicionario2.copy())
print(oDict1 == oDict2) #False
