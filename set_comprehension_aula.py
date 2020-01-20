"""
Set comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""
# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Faca uma alteracao na estrutura acima para gerar um dicionario ao inves de um set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Finalizando com mais um exemplo
letras = {letra for letra in 'Geek University'}
print(letras)
