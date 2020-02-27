"""
O bloco with

Ele abre, executa o que foi pedido no with e ja fecha o arquivo.
"""

with open("texto.txt") as arquivo:
    print(arquivo.read())
