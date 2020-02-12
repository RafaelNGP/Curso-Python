# using recursion to implement power and factiorial functions


def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num ** pwr


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


print(f"{5} to the power of {3} is {power(5, 3)}")
print(f"{5} to the power of {3} is {power(6, 3)}")
print(f"{5} to the power of {3} is {power(7, 3)}")
print(f"{1} to the power of {5} is {power(1, 5)}")
print(f"{4}! is {factorial(4)}")
print(f"{0}! is {factorial(0)}")