"""
Variaveis locais e globais

Inicialmente esta nao era uma aula separada, mas criei este arquivo para testar.
"""
instrutor = "Geek - Global"
print(instrutor)


def diz_oi():
    instrutor = "Alguem - Local"
    return print(instrutor)


diz_oi()
print(instrutor)
