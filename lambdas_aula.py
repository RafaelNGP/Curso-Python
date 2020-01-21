"""
Utilizando Lambdas
Mais utilizado em filtragem e ordenacao de dados, porem nao limitado a isso.

Conhecidas por expressoes lambdas, ou simplesmente lambdas, sao funcoes sem nome, ou seja,
funcoes anonimas.

Funcao em python
def soma(a, b):
    return a + b

# Expressao lambda
calc = lambda x: 3 * x + 1

Funcao quadratica
f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c)

"""
# Expressao lambda
calc = lambda x: 3 * x + 1

# Como utilizar a lambda?
print(calc(4))
print(calc(7))

# Podemos ter lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo("   rafael ", " ferreira "))

# Em funcoes python podemos ter nenhuma ou varias entradas. Em Lambdas tambem.
amar = lambda: 'como nao amar python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x2, ,,,, xn: <expressao>

print(uma(5))
print(duas(5, 2))
print(tres(5, 6, 7))
print(amar())

# Outro exemplo
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert',
           'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Definindo a funcao


def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))
