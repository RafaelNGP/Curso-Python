"""
Documentando funcoes com docstrings

OBS: Podemos ter acesso a documentacao de uma funcao em python utilizando
a propriedade especial __doc__

Podemos ainda fazer acesso a documentacao com a funcao help()
"""


def diz_oi():
    """Uma funcao simples que retorna uma string com o conteudo 'Oi'"""
    return 'Oi'


# O conteudo que eh mostrado nesta chamada eh o docstring da funcao.
# print(help(print()))
print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)
