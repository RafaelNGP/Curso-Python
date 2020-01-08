"""
Modulo Collections - Deque
Podemos dizer que o deque eh uma lista de alta performance
"""
from collections import deque

# criando deques
deq = deque("Geek")
print(deq)

# Adicionando elementos no deque
deq.append("y")
deq.appendleft('K')
print(deq)

# Removendo elementos
deq.pop()
print(deq.pop())
deq.popleft()
print(deq)
