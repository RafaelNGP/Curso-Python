"""
Onde as variaveis comecam e terminam
"""
# Variavel criada e executada
numero = 42
print(numero)

if numero > 42:
    novoNumero = 42
    print(novoNumero)

# Gera erro, pois a variavel novoNumero nunca foi criada neste escopo, afinal ela esta dentro do if que n foi chamado.
print(novoNumero)