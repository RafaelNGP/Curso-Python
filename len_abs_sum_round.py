"""
Len, Abs, Sum, Round

len() - Retorna o tamanho (o numero de itens) de um iteravel
Abs() - Retorna o valor absoluto de um numero inteiro ou real. De forma basica seria seu valor real
sem o sinal.
Sum() - Recebe como parametro um iteravel, podendo receber um valor inicial e retorna a soma total
dos elementos, incluindo o valor inicial.
    OBS: O valor inicial default eh 0.
Round() - Retorna um numero arredondado para n digito de precisao apos a casa decimal. Se a precisao
nao for informada retorna o inteiro mais proximo da entrada.
"""
print(len('Geek University'))
print(len([1, 2, 3, 4]))
print(len({0, 1, 2, 3, 4}))

# Por debaixo dos panos, quando utilizamos a funcao len() o python faz o seguinte:
# Dunder len
print('Geek University'.__len__())
print()

# ABS
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

# Round
print(round(10.2))
print(round(3.14))
print(round(10.5))
print(round(10.6))
print(round(1.212121, 2))
print(round(1.219990, 2))
