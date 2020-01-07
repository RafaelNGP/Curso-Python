"""
Conhecidos como Dicionarios

Dicionarios em Python sao representados por chaves {}
"""
receita = {'jan': 100, 'fev': 200, 'mar': 400, 'abr': 150, 'mai': 180, 'jun': 850, 'jul': 100, 'ago': 190,
           'set': 800, 'out': None, 'nov': 80, 'dez': 135}

# Iterar sobre dicionarios
for chave in receita:
    print(chave)
for chave in receita:
    print(receita[chave])
for chave in receita:
    print(f"Chave: {chave} - Valor: {receita[chave]}")
for chave, valor in receita.items():
    print(f"Chave: {chave} - Valor: {receita[chave]}")

print(receita.keys())
print(receita.values())
print(receita.items())

for chave in receita.keys():
    print(f"Chave: {chave} - Valor: {receita[chave]}")
