# Try out the Python queue functions
from _collections import deque

# Create a new empty stack
queue = deque()

# Push itens onto the stack
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Print the stack contents
print(queue)

# pop an item off the stack
print(queue.popleft())
print(queue.pop())
