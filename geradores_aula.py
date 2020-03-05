"""
Geradores

- Geradores (Generators) sao iterators.

Outras informacoes
    - Generators podem ser criados com funcoes geradoras
    - Funcoes geradores utilizam a palavra yield


            Diferencas entre funcoes e gerenator functions
-------------------------------------------------------------------------
/ funcoes                           generator functions                 /
-------------------------------------------------------------------------
/ utilizam return                   utilizam yield                      /
-------------------------------------------------------------------------
/ Retorna uma vez                   pode usar yield multiplas vezes     /
-------------------------------------------------------------------------
/ qnd executada, retorna um valor   qnd executada, retorna um generator /
-------------------------------------------------------------------------
"""
# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: uma generator function nao eh um generator, ela GERA um generator


gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print()
gen = conta_ate(10)
for n in gen:
    print(n)


print()
gen = conta_ate(10)
print(next(gen))
print()
for n in gen:
    print(n)

print()
gen = list(conta_ate(10))
print(gen)
