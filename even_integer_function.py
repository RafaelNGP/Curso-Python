# function solition
def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result


# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


print(even_integers_function(10))
print(list(even_integers_generator(10)))
