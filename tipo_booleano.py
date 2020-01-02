"""
Tipo Booleano

2 constantes = Verdadeiro ou falso
True ou False

OBS: Sempre com a inicial maisucula.

# >>> num2 = 2
# >>> num3 = 4
# >>> num2 > num3
# False
# >>> num3 <= num2
# False

# >>> type(True)
# <class 'bool'>
"""
print("Atribuindo valor True para 'ativo'")
ativo = True
logado = False

print(ativo)
"""
Operacoes basicas
"""
# Negacao (not)
print("Printando a negacao do valor de ativo")
print(not ativo)

# Ou (or)
"""
>>> True or True = True
>>> True or False = True
>>> False or True = True
>>> False or False = False
"""
print(ativo or logado)

# E (and)
"""
>>> True and True = True
>>> True and False = False
>>> False and True = False
>>> False and False = False
"""
