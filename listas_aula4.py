# Utilizando listas com variaveis
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
cores = ["Verde", "Amarelo", "Azul", "Branco"]
print(cores[0])
# print(cores[1])
print()

# Exemplo proprio
for cor in cores:
    print(cor, end=" ")

# Fazemos acesso em ordem inversa
print()
print(cores[-1])
print(cores[-2])

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Exemplo proprio, encontrando o indice de um valor especificado
print(cores.index("Verde"))

# Receber valor e indice por um laco for
for indice, valor in enumerate(cores):
    print(indice, valor)

numeros = list(range(11))
numeros.append(5)
primeiroValor = numeros.index(5)
print()
print(numeros)
print(primeiroValor)
print(numeros.index(5, primeiroValor+1))

print()
print(numeros[::2])

print()
print(numeros)
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(len(numeros))

# Transformar lista em tupla
print()
print(numeros)
print(type(numeros))
tupla = tuple(numeros)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12 = numeros
print(num1)
print(num2)
print(num3)
print(num4)

# Copia de listas para outra (shallow copy e deep copy)
# Forma 1 (Deep Copy)
lista = [1, 2 , 3]
print()
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print()
print(lista)
print(nova)
# Assim temos duas listas independentes.
lista.clear()
nova.clear()

# Forma 2 (Shallow Copy)
print()
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)
nova.append(4)

print()
print(lista)
print(nova)
# Dessa forma as duas listas estao intimamente ligadas
