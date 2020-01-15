"""
Loop For

C ou Java
for (int i = 0; i < limitador; i++){
    //codigo

Python

For item in interavel:
    //codigo

utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis
-Strings
-Listas
-Range
"""

nome = "Geek University"
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1, 10):
    print(numero)

for valor in enumerate(nome):
    print(valor)

print("A regra do jogo eh a seguinte: Cada vez que repetir, sera somado o numero de vezes repetidas!")
soma = 0
qnt = int(input("Quantas vezes o loop deveria rodar? "))

for vezes in range(1, qnt+1):
    soma += vezes
    print([vezes, soma])

soma = 0
for vezes in range(1, qnt+1):
    soma += vezes
    print(f"Somando pela {vezes} vez, o total eh {soma}")

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

# Testando os conceitos de List Comprehension
soma = 0
print([f'Somando pela {vezes} vez, o total eh {soma}' for vezes in range(1, qnt+1)])
# Assim consigo iterar a frase no range ... mas e a soma?
