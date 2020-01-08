"""
Modulo Collections - Default Dict

Recap dicionarios
dicionario = {"Curso": "Programacao em Python: Essencial"}
print(dicionario)
print(dicionario['Curso'])
# print(dicionario['teste']) #KeyError

Default dict -> Ao criar um dicionario usando o default dict, nos informamos um valor default a ele, podendo
utilizar lambida para isso. Este valor sera utilizado sempre que nao houver um valor definido. Caso tentemos
acessar uma chave que nao existe, essa chave sera criada e o valor default sera atribuido.

OBS: Lambdas sao funcoes sem nome, que podem ou nao receber parametros de entrada e retornar valores.
"""
# Import da colecao
from _collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = "Programacao em Python: Essencial"
print(dicionario)
print(dicionario['outro'])
print(dicionario)
