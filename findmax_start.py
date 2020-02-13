# use a recursive algorithm to find a maximum value
def find_max(item):
    if len(item) == 1:
        return item[0]

    op1 = item[0]
    print(op1)
    op2 = find_max(item[1:])
    print(op2)
    if op1 > op2:
        return op1
    else:
        return op2


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(find_max(items))
