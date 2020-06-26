# Implemente um programa que receba 10 valores em um vetor de inteiros.
# Após isso, exiba a soma desses valores, a média, o menor valor informado e o maior valor informado.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# forma roots
total = 0
for linha in lista:
    total += linha
print(total)

# forma facil
print(sum(lista))
print(min(lista))
print(max(lista))
print(sum(lista) / len(lista))

# vetores bidimencionais (matrizes)
lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(lista[0][1])

print()
for linha in lista:
    for valor in linha:
        print(valor)

print()

textoNomes = {1: 'Jane', 2: 'Tim', 3: 'Mia', 4: 'Sam', 5: 'Leo', 6: 'Ted',
              7: 'Bea', 8: 'Lou', 9: 'Ana', 10: 'Max', 11: 'Zoe'}

for chave, valor in textoNomes.items():
    if valor == 'Ana':
        print(f"Ela foi encontrada na posição: {chave}")

print()

retorno = -1
vetor = [11, 21, 31, 41, 51]
valor = int(input("Informe um valor para busca: "))
for n in vetor:
    retorno += 1
    if valor == n:
        print(f"Valor encontrado no index {retorno}")

aux = 0
lista = [9, 20, 17, 10, 18, 25, 25, 15, 2, 15, 17, 17, 16, 11, 3, 11, 25, 16, 12, 22,
         24, 14, 8, 16, 21, 27, 27, 18, 1, 29, 16, 10, 0, 2, 2, 26, 19, 9, 12, 24, 20,
         3, 16, 4, 4, 11, 9, 21, 25, 6, 25, 10, 29, 20, 17, 23, 3, 26, 0, 30, 4, 20, 7,
         11, 11, 19, 21, 4, 24, 13, 9, 29, 10, 22, 6, 28, 29, 28, 22, 10, 17, 3, 1, 1, 18,
         2, 3, 11, 12, 28, 28, 7, 30, 25, 17, 28, 21, 12, 5, 12]
for n in range(len(lista) - 1, 0, -1):
    for m in range(n):
        if lista[m] > lista[m+1]:
            aux = lista[m]
            lista[m] = lista[m+1]
            lista[m+1] = aux

print(lista)
