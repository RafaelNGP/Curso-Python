"""
Teste de velocidade com Empressoes geradoras

"""
import time

# generators (geradores)
def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)
print(next(ge1))
print(next(ge1))
print(next(ge1))


print()
# generator expression
ge2 = (num for num in range(1, 10))
print(ge2)
print(next(ge2))
print(next(ge2))
print(next(ge2))


print()
# somando todos os valores
print(sum(num for num in range(0, 10)))

# realizando o teste de velocidade
# generator expression

gen_inicio = time.time()
print(sum(num for num in range(0, 100000000)))
gen_tempo = time.time() - gen_inicio

# list comprehension
list_inicio = time.time()
print(sum(num for num in range(0, 100000000)))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou: {gen_tempo}\n'
      f'List Comprehension levou: {list_tempo}')
