"""
**kwargs

Pode ser chamado por qualquer nome, porem o uso desse nome eh uma convencao no
mundo dos programadores

Este eh so mais um parametro, mas diferente do *args, que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parametros nomeados, e transforma
esses parametros extras em um dicionario.

Nas nossas funcoes, podemos ter:
    -Parametros obrigatorios
    -*args
    -Parametros default
    -**kwargs
"""


def cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print(f"A cor favorita de {nome} eh {cor}")


cores_favoritas(marcos="verde", laura="amarelo", max="azul", gustavo="branco")

# Ex mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == "python":
        return "voce recebeu um cumprimento pythonico Geek!"
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Nao tenho certeza de quem eh voce"


print()
print(cumprimento_especial())
print(cumprimento_especial(geek="python"))
print(cumprimento_especial(geek="Oi"))
print(cumprimento_especial(geek="especial"))


def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs)


print(minha_funcao(8, 'Julia'))
print(minha_funcao(18, "Felicity", 4, 5, 6, solteiro=True))
print(minha_funcao(34, 'Felipe', eu='Nao', voce='Vai'))
print(minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True))
print(minha_funcao(27, "Rafael Abud Ferreira", "Sempre sao 3", solteiro=True, aprendendo="Com certeza"))


def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a=0, b=0, c=0):
    return print(a+b+c)


lista = [1, 2, 3]
tupla = 1, 2, 3
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)
dicionario2 = {'a': 1, 'b': 2, 'c': 3}

print(soma_multiplos_numeros(*lista))
print(soma_multiplos_numeros(*tupla))
print(soma_multiplos_numeros(*conjunto))
print(soma_multiplos_numeros(**dicionario))
print(soma_multiplos_numeros(**dicionario2))

# OBS: Os nomes da chave em um dicionario devem ser o mesmo dos parametros da funcao.
