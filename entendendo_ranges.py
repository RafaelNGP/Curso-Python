"""
Ranges

-Precisamos conhecer o Loop for para usar os Ranges
-Precisamos conhecer o Range para trabalhar melhor com loops for.

Range eh utilizado para gerar sequencias numericas, nao aleatorias, mas sequencial.

Formas gerais:

# Forma 1
range(valor_de_parada)

# Forma 2
range(valor_de_inicio, valor_de_parada)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)

# Forma 4 (inverso do 3)
range(valor_de_inicio, valor_de_parada, passo)

"""

for num in range(11):
    print(num)

for num in range(5, 11):
    print(num)

for num in range(0, 11, 2):
    print(num)

for num in range(10, 0, -1):
    print(num)