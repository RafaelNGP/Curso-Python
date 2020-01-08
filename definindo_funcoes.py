"""
Definindo Funcoes

- Funcoes sao pequenos trechos de codigo que realizam tarefas especificas.
    - Ja utilizamos varias funcoes desde que iniciamos este curto.
        -print()
        -len()
        -max()
        -min()
        -count()
        -e muitas outras...
    - Pode ou nao receber entradas de dados e retornar uma saida de dados.
    - Sao muito uteis para executar procedimentos similares por repetidas vezes.

    OBS: Se voce escrever uma funcao que realize diversas tarefas dentro dela, pode ser bom
    fazer uma verificacao para que a funcao seja simplificada.
"""
# Exemplo de utilizacao de funcoes:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utizando a funcao integrada (built-in) do python print()
# print(cores)
# cores.append('roxo')
# print(cores)
# print(help(print))
# Mas entao, como definir funcoes?
"""
Em Python, a forma geral de definir uma funcao eh:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
onde:
    - nome_da_funcao -> SEMPRE com letras minusculas e se for nome composto, separado por _ (Snake Case)
    - parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula
    - bloco_da_funcao -> Tambem chamado de corpo da funcao ou implementacao, onde o processamento da funcao acontece,
    neste bloco, pode ter ou nao um retorno da funcao.
    
Veja que para definir uma funcao, utilizamos a palavra reservada "def" informando ao Python que estamos definindo
uma funcao. Tambem abrimos o bloco de codigo com o ":"
"""
# Definindo a primeira funcao


def diz_oi():
    print("oi!")


"""
OBS: 
1 - Veja que dentro das nossas funcoes, podemos utilizar outras funcoes.
2 - Veja que nossa funcao so executa uma tarefa, ou seja, a unica coisa que ela faz eh dizer oi.
3 - Veja que esta funcao nao recebe nenhum parametro de entrada.
4 - Veja que esta funcao nao retorna nada.
"""

# Utilizando funcoes
diz_oi()

# Exemplo 2


def cantar_parabend():
    print('Parabens vagabundo')
    print('Nesta data maldita')
    print('Muitas enfermidades')
    print('Muito odio na vida')


for n in range(5):
    print(n)
    cantar_parabend()

# Em Python, podemos inclusive criar variaveis do tipo de uma funcao e executar esta funcao atravez da variavel
cantar = cantar_parabend
cantar()
