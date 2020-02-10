"""
Find the greatest common denominator of two numbers - LinkedIn Learning
Using Euclid`s algorithm
"""


def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a


print(gcd(60, 96))  # 12
print(gcd(20, 8))   # 4
