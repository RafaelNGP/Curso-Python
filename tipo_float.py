"""
Tipo Float

Tipo real, decimal

casas decimais

OBS? o separador de casas decimais eh ponto e nao virtula.
"""
# Criando float
valor = 1.44
print(valor)
print(type(valor))

# Cria uma tupla em vez de float
valorTupla = 1, 44
print(valorTupla)
print(type(valorTupla))

# Evitar dupla atribuicao
valor1,  valor2 = 1, 44
print(valor1)
print(valor2)

# Convertendo valores
res = int(valor)
print(valor)
print(type(valor))

# Podemos trabalhar numeros complexos
# >>> var = 5j
# >>> type(var)
# <class 'complex'>
# >>> var ** 2
# (-25+0j)