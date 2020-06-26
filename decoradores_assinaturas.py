"""
Decorators com diferentes assinaturas

Para resolver, utilizamos um padrao de projeto usando decorator patterns


"""


# relembrando
def gritar(funcao):
    def aumentarNome(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentarNome


@gritar
def pessoa(nome):
    return f'meu nome eh {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'


print(pessoa('Rafael'))
print(type(pessoa))

print(ordenar('Yakisoba', 'burgers'))
