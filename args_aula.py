"""
Entendendo o *args

    - Eh um parametro, como outro qualquer. Isso significa que voce podera chamar de qualquer
    coisa, desde que comece com *

    por ex:
    *xis

    mas por convencao, todos utilizam *args para defini-li.

O QUE EH O ARGS??
    O parametro *args utilizado em uma funcao, coloca os valores extras informados como entrada
    em uma tupla, entao desde ja lembre-se que as tuplas sao imutaveis.
"""


def soma_todos_os_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_os_numeros(4, 6, 9))

# Entendendo o Args


def soma_todos_os_atributos(*args):
    return sum(args)


print(soma_todos_os_atributos())
print(soma_todos_os_atributos(8))
print(soma_todos_os_atributos(9, 8))
print(soma_todos_os_atributos(9, 5, 3))
print(soma_todos_os_atributos(7, 8, 2, 9))
# print(soma_todos_os_atributos(8, 6, "AHAL"))


def cadastro_usuario(*args):
    nome = input("Qual o nome que sera cadastrado? ")
    email = input("Informe seu email: ")
    idade = int(input("Qual sua idade? "))
    tipo_conta = input("Que tipo de contavai abrir? (User/ADM) ")
    if idade >= 18:
        idade = "Maior de idade"
    else:
        idade = "Menor de idade"
    print(f'\n{tipo_conta} {nome} cadastrado com sucesso!\n'
          f'{idade}\n'
          f'Email para contato: {email}')
    print(args)

# print(cadastro_usuario(nome, email, idade, tipo_conta, "Periodo de Testes", 3.14))


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return print("Seja bem vindo, Geek!")
    return print("Nao tenho certeza de quem eh voce")


# verifica_info()
# verifica_info("Geek", "University")
# verifica_info("University", 3.14, 'Geek')

# O * serve para que informemos ao python que estamos passando como argumento
# uma colecao de dados. Desta forma, ele sabera que vai precisar desempacotar os dados antes.
numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_os_atributos(*numeros))
