"""
Modulos built-in (modulos integrados, que ja vem instalados no Python)

# Utilizando alias (apelidos) para modulos/funcoes
import random as rdm
print(rdm.random())

# Podemos importar todas as funcoes de um modulo utilizando o *
from random import *
print(random())

# Importando o modulo inteiro
import random
print(random.random())

# Importando uma funcao e dando um apelido.
from random import randint as rdi
print(rdi(5, 89))

# Importando uma funcao e dando um apelido.
from random import randint as rdi, random as rdm
print(rdm())
"""

from random import (
    random,
    randint,
    shuffle,
    choice
)

lista = ["Pedra", "Papel", "Tesoura"]

print(random())
print(randint(1, 60))
shuffle(lista)
print(lista)
print(choice("qwertyuiopasdfghjklzxcvbnm"))
