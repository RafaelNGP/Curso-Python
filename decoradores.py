"""
Decorators

O que sao decorators?
    - Sao funcoes.
    - envolvem outras funcoes e aprimoram seus comportamentos
    - Tambem sao exemplos de HOF
    - Tem uma sintaxe propria usando "@" >- systact sugar -<


/---------------------------------------/
/           function decorator          /
/---------------------------------------/
                    +
/---------------------------------------/
/                funcao                 /
/---------------------------------------/
                    =
//-------------------------------------//
/---------------------------------------/
/           funcao decorada             /
/---------------------------------------/
//-------------------------------------//

"""


# Decorators como funcoes
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce.')
        funcao()
        print('Tenha um otimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) a geek university')


pessoa = seja_educado(saudacao)
pessoa()


# Testando 2
def raiva():
    print('EU TE ODEIO')


raiva_educada = seja_educado(raiva)
raiva_educada()


# Decorators com Syntax Sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer vc!')
        funcao()
        print('tenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('meu nome eh Pedro')


# testando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir')


dormir()
print()

