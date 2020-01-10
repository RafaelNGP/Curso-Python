"""
Funcoes com parametro padrao

-funcoes onde a passagem de parametros seja opcional
"""


def esponencial(numero, potencia=2):
    return numero ** potencia
# Se o usuario passar apenas um argumento, este sera atribuido ao parametro numero, e o parametro
# potencia sera igual a 2, em caso de nenhum outro argumentos, o segundo sera sempre o valor 2.


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor == True:
        return f"Seja bem vindo, Professor {nome}"
    elif nome == 'Geek':
        return f'Achei que fosse um instrutor ... estranho'
    return f'Seja bem vindo, {nome}!'


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def conta(num1, num2, fun=soma):
    return fun(num1, num2)


print(mostra_informacao())
print(mostra_informacao("Rafael"))
print(mostra_informacao("Geek", True))

# Uma funcao pode receber tambem como valor default uma outra funcao.
print(conta(1, 2))
print(conta(1, 2, subtracao))