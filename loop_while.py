"""
Loop while

Iterar sobre uma frequencia previamente desconhecida

While expressao_booleana:
    codigo

O bloco do while sera repetido enquanto a expressao booleana for verdadeira.
"""

# Ex 1
numero = 0
while numero <= 10:
    print(numero, end=' ')
    numero += 1

# Em um loop while eh importante que cuidemos do criterio de parada - (Loop infinito)

resposta = ''
while resposta != "s":
    resposta = input("Ja acabou Jessica? ")