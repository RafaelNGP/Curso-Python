"""
Leitura de Arquivos

Para o conteudo de um arquivo em Python, utilizamos a funcao integrada open()

open() -> Na forma mais simples de utilizacao nos passamos apenas um parametro de entrada, que neste caso
eh o nome do arquivo a ser lido. Essa funcao retorna um _io.TextIOWrapper e eh com ele que trabalhamos entao.

https://docs.python.org/3/library/functions.html
"""
arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo)
print(arquivo.read())
print(type(arquivo))
