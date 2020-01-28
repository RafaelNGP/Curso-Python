"""
Try/Except

utilizamos para tratar erros que podem ocorrer no nosso codigo. Previnindo assim que o programa pare
de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples eh:

try:
    //execucao problematica
except:
    //O que deve ser feito em caso de problemas.
"""

# exemplo 1 - Tratando um erro generico
try:
    geek()
except NameError as err1:
    print(f"A funcao nao foi definida. Erro: {err1}")
except TypeError as err2:
    print(f"Utilizando o tipo de dado errado. Erro: {err2}")
except ValueError as err3:
    print(f"Nao recebe um valor esperado. Erro: {err3}")

# Em resumo: Tente executar a funcao, caso encontre erros, imprima o outro bloco em vez disso.
