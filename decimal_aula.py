"""
Usando casas decimais para realizar contas.

Curso Python Essencial Training no LinkedIn Learning
"""

# Depois de fazer a conta sem o import de decimal, fiz o import aqui
from decimal import *

x = .1 + .1 + .1 - 0.3
print(f'x is {x}')
print(type(x))

a = Decimal('.10')
b = Decimal('.30')
y = a + a + a - b

print(y)
print(type(y))

# x is 5.551115123125783e-17
# <class 'float'>

# Doideira, certo? Sem o uso da ferramenta certa eh impossivel fazer essas contas com precisao.
