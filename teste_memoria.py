"""
Teste de memoria com generators

Sequdncia de fibonachi
1, 1, 2, 3, 5, 8, 13...

"""


def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste usando listas
for n in fib_lista(10000):
    print(n)    # 8.7 MB

input()


def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador += 1


# teste com geradores.
for n in fib_gen(10000):
    print(n)    # 3.7 MB

input()
