"""
Try/Except/Else/Finally

utilizamos para tratar erros que podem ocorrer no nosso codigo. Previnindo assim que o programa pare
de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples eh:

try:
    // execucao problematica
except:
    // O que deve ser feito em caso de problemas.
else:
    // Executado apenas se nao ocorrer o erro.
finally:
    // sempre eh executado, independente de ter tido um erro ou nao.
Quando e onde tratar codigo: Toda entrada deve ser tratada.
"""
# exemplo 1 - Tratando um erro generico
try:
    geek()
except NameError as err1:
    print(f"A funcao nao foi definida. Erro: {err1}")
except TypeError as err2:
    print(f"Utilizando o tipo de dado errado. Erro: {err2}")
except ValueError as err3:
    print(f"Nao recebe um valor esperado. Erro: {err3}")

# Em resumo: Tente executar a funcao, caso encontre erros, imprima o outro bloco em vez disso.

try:
    num = int(input("informe um numero: "))
except ValueError as erro1:
    print('Valor incorreto')
else:
    print(f'voce digitou: {num}')

# exemplo mais complexo


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Valor incorreto. Erro: {err}"


num1 = input('Informe o primeiro numero: ')
num2 = input("Informe o segundo numero: ")

print(dividir(num1, num2))

