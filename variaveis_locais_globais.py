"""
Variaveis locais e globais

Inicialmente esta nao era uma aula separada, mas criei este arquivo para testar.
"""


def diz_oi():
    instrutor = "Alguem - Local"
    return print(instrutor)


def diz_oiLocal():
    global instrutor
    # Ao invocar o global, ele esta mudando o valor da variavel global dessa forma e nao da local.
    instrutor = "Geek" + " - Local"
    return print(instrutor)


instrutor = "Geek - Global"
print(instrutor)

diz_oi()
diz_oiLocal()
print(instrutor)
