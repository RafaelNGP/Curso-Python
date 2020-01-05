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

# Ex 2
numero = 0
print()
while numero <= 10:
    if numero == 6:
        break
    print(numero, end=' ')
    numero += 1

# Em um loop while eh importante que cuidemos do criterio de parada - (Loop infinito)
# Ex 3
print()
resposta = ''
while resposta != "s":
    resposta = input("Ja acabou Jessica? ")

# Ex 4
while True:
    comando = input("Digite 'sair' para sair: ").lower()
    if comando == "sair":
        break
