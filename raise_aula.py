"""
Raise - Levantando os proprios erros.
OBS: Nao eh uma funcao, mas sim uma palavra reservada.

Para simplificar: Pense no raise como sendo util para que possamos criar nossas proprias excessoes e mensagens
de erro.

A forma mais geral de uso:
raise TipoDoErro('Mensagem de erro')

O raise, assim como o return, finaliza a funcao. Ou seja, nada apos do raise eh executado.
"""


def colore(texto, cor):
    cores = ("verde", "amarelo", "azul", "branco")
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma String")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma String")
    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")
    print(f'O texto {texto} sera impresso na cor: {cor}')


colore('geek', 'preto')
