"""
getsizeof ()

Resolvi fazer um arquivo separado para esse import
"""
from sys import getsizeof

# Exemplos
# Comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof(x * 10 for x in range(1000))

# Prints
print(f'Tamanho de cada lista, em bytes:\n'
      f'Lista: {list_comp} bytes\n'
      f'Set: {set_comp} bytes\n'
      f'Dict: {dict_comp} bytes\n'
      f'Generator: {gen} bytes')

gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)
