"""
Pacotes

Diferenca entre Modulos e Pacotes:
    Modulo -> Apenas um arquivo Python que pode conter diversas funcoes para utilizarmos.
    Pacote -> Eh um diretorio contendo uma colecao de modulos.

Nas versoes 2.x Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
Nas versoes 3.x Python, nao eh mais obrigatoria a utilizacao deste arquivo, mas normalmente ainda
eh utilizado para manter compatibilidade.
"""

from geek import geek1, geek2
from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4, 6))
print(geek2.curso)
print(geek2.funcao2())
print(geek3.funcao3())
print(geek4.funcao4())
